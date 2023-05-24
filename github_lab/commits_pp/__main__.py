import requests
import sys

str_user = sys.argv[1]
str_repo = sys.argv[2]
str_url_api_contributors = "https://api.github.com/repos/{}/{}/contributors"
response = requests.get(str_url_api_contributors.format(str_user,str_repo))
list_contributor_logins = (list(map(lambda x: x["login"], response.json())))
#print(list_contributor_logins)

str_url_api_commits = "https://api.github.com/repos/grafana/grafana/commits?branch=master&since=2021-12-03&until=2021-12-10"
response = requests.get(str_url_api_commits)
list_commits_logins = (list(map(lambda x: x["author"]["login"], response.json())))
print (list_commits_logins)
# TODO: use graphql?
# /repos/:owner/:repo/commits/master
# https://docs.github.com/en/rest/guides/basics-of-authentication
# https://docs.github.com/en/rest/overview/resources-in-the-rest-api