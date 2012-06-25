#!/usr/bin/env python
# COM-380 work

import requests
import simplejson as json
import sys

def main():
    if len(sys.argv) != 3:
        print "Need two args. First: a github username. Second: a project name.\n"
        sys.exit(1)

    ### Center user & project
    user = sys.argv[1] 
    repo = sys.argv[2] 
    #user = "ruoranwang"
    #repo = "IITVs"

    ### first circle users
    print "a"
    user_list = get_watchers(user, repo)
  
    ### repos of first circle
    dict_of_repo_list = {}  # {'ruoranwang': [a,b,c,d], 'yan': [e,d,f,g]}
    for user in user_list:
        print user[1]
  
    sys.exit(1)
    ### second circle users
    for user, repos in dict_of_repo_list.iteritems():
        for item in repos:
            print "User: {}, Repo: {}".format(user, item),
            print get_watchers(user, item)
            print 

def get_repos(user):
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
    print json_list
    for watcher in json_list:
        watchers.append(str(watcher['login']))
    return watchers

if __name__ == "__main__":
    main()
