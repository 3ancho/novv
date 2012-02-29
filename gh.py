#!/usr/bin/env python
import requests
import simplejson as json
import sys

def main():
    if len(sys.argv) != 3:
        print "Need two args.\n"
        sys.exit(1)
    user = sys.argv[1] 
    repo = sys.argv[2] 
    #user = "ruoranwang"
    #repo = "IITVs"
    user_list = get_watchers(user, repo)
   
    list_repo_list = [] 
    for user in user_list:
        list_repo_list.append( get_repos(user) )
    
    for repo_list in list_repo_list:
        for item in repo_list:
            print "User: {}, Repo: {}".format(item[0],item[1]),
            print get_watchers(item[0],item[1])
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
    for watcher in json_list:
        watchers.append(watcher['login'])
    return watchers


if __name__ == "__main__":
    main()
