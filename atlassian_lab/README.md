# Atlassian Lab
## Access with API Token
* Create API Token
    * https://id.atlassian.com/manage-profile/security/api-tokens
* Add token to atl.conf file
```
[atlassian_api_client]
user=YOUR_EMAIL_ADDRESS
api_token=YOUR_ATLASSIANAPI_TOKEN
server=YOUR_SERVER_URL_WITH_HTTPS_AT_START
issue_key=YOUR_ISSUE_KEY
```

## JQL
```
project = "TEST" and created >= startOfDay(-17d) and status = 'kaizen' ORDER BY created DESC
```