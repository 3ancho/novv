#!/usr/bin/env python
# COM-380 work
import requests
from gh import get_followers
import pickle, sys
def main():
    if len(sys.argv) != 2:
        print "Need one args pickle.\n"
        sys.exit(1)
    p = sys.argv[1]
    if "." not in p:
        p += ".pkl"
    pname = p.split(".")[0]
    print p
    f = open(p, "rb")
    user_list = pickle.load(f)

    connections = {}

    r = requests.head("https://api.github.com")
    count = int(r.headers['x-ratelimit-remaining'])

    for user in user_list:
        for follower in get_followers(user):
            count -= 1
            if count == 1:
                break
            key = "{},{}".format(user, follower)
            if key in connections:
                connections[key] += 1
            else:
                connections[key] = 1

    f_dict = open("{0}_output.pkl".format(pname), "wb")
    pickle.dump(connections, f_dict)
    f_dict.close()

    f = open("{0}.dat".format(pname), "w")
    for key, value in connections.iteritems():
        f.write("{}, {}\n".format(key, value))
    f.close()

if __name__ == '__main__':
	main()
