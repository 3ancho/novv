#!/usr/bin/env python
# COM-380 work

import requests
import simplejson as json
import sys
import pickle

def main():
    if len(sys.argv) != 3:
        print "Need two args.\n"
        sys.exit(1)
    user = sys.argv[1] 
    repo = sys.argv[2] 
    #user = "ruoranwang"
    #repo = "IITVs"
    v2ex = Repo(user, repo)
    watchers = []
    while 1:
        temp = v2ex.watchers()
        if temp == 0:
            print "done"
            break
        watchers.extend(temp)
    output = open("watchers.pkl", "wb")
    pickle.dump(watchers, output)
    output.close()
    

#    user_list = get_watchers(user, repo)
#    list_repo_list = [] 
#    for user in user_list:
#        list_repo_list.append( get_repos(user) )
#   
#    connects = {} 
#
#    for repo_list in list_repo_list:
#        for item in repo_list:
#            for user in get_watchers(item[0],item[1]):
#                if user == item[0]:
#                    continue
#                key = "{},{}".format(item[0],user)
#                print key
#                if key in connects:
#                    connects[key] += 1
#                else:
#                    connects[key] = 1
#
#    f = open("gh.dat","w")
#    for key, value in connects.iteritems():
#        f.write("{}, {}\n".format(key, value))
#    f.close()

class Repo():
    def __init__(self, user, repo):
        self.base_url = "https://api.github.com/repos/{user}/{repo}/watchers?page={page_number}&per_page=100"
        self.page_number = 1
        self.last = False
        self.user = user
        self.repo = repo

    def watchers(self):
        request_url = self.base_url.format(user=self.user, repo=self.repo, page_number=self.page_number)
        r = requests.get(request_url)
        if len(r.content) <= 3:
            return 0
        json_list = json.loads(r.text)
        watchers = []
        for watcher in json_list:
            watchers.append(watcher['login'])
        self.page_number += 1
        print watchers
        return watchers

def get_repos(user):
    ''' return a tuple (user, repo) '''
    repos = []
    r = requests.get("https://api.github.com/users/{user}/repos"\
                    .format(user=user))
    json_list = json.loads(r.text)
    for repo in json_list:
        repos.append([user, repo["name"]])
    return repos

def get_watchers(user, repo):
    watchers = []
    r = requests.get("https://api.github.com/repos/{user}/{repo}/watchers"\
                    .format(user=user, repo=repo))
    json_list = json.loads(r.text)
    for watcher in json_list:
        if watcher['login'] != user:
            watchers.append(watcher['login'])
    return watchers

if __name__ == "__main__":
    main()
