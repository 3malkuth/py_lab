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

## TODO
* Report how many SP's added in a sprint
* Report how many bugs added versus closed
  * Last Sprint
  * Last Quarter
  * Last Year

## JQL
```
# Bug Reports
# Get a list of issues that
# were created in the last number of days
# and have the label 'kaizen'
project = 'TEST' and created >= startOfDay(-17d) and labels = 'kaizen' ORDER BY created DESC
# Other options...
project = 'TEST' and created >= startOfDay() and issuetype = 'Bug' ORDER BY created DESC
project = 'TEST' and created >= startOfMonth() and issuetype = 'Bug' ORDER BY created DESC
project = 'TEST' and created >= startOfYear() and issuetype = 'Bug' ORDER BY created DESC
project = 'TEST' and created >= startOfDay(-17d) and issuetype = 'Bug' ORDER BY created DESC
project = 'TEST' and created >= startOfDay(-3M) and issuetype = 'Bug' ORDER BY created DESC
# This will include everything in the months that this range touches...
project = 'TEST' and created >= startOfMonth(-3M) and issuetype = 'Bug' ORDER BY created DESC
# This will include everything in the years that this range touches...
project = 'TEST' and created >= startOfYear(-6M) and issuetype = 'Bug' ORDER BY created DESC
# Get Bugs created and closed from a particular date
project = 'TEST' and created >= startOfYear(-6M) and status in ('DONE') and issuetype = 'Bug' ORDER BY created DESC
# Get Bugs created and closed in a date range
project = 'TEST' and created >= startOfYear(-6M) and created <= startOfDay(-30d) and status in ('DONE','WONT_DO') and issuetype = 'Bug' ORDER BY created DESC
```
