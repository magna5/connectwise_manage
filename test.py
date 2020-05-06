# Simple script to test the LM_GET method from interactive python
#
# usage:  `from test import results`
# Then view and manipulate results and results['items']

from connectwise_scrape import LM_GET

queryParams =  {"filter": "hostGroupIds~4"} # {"fields": "id,name,displayName,hostGroupIds,customProperties,systemProperties,autoProperties,inheritedProperties"}
lm_creds = {"_lm_id": "fWTk7rvkN8dqqaT3stPB", "_lm_key": "85pc+h2K9547}]cY8hNsR)^4%)x(9sc~4qdI(M+{", "_lm_account": "magna5global"}

results = LM_GET(_resource_path = '/device/devices', _query_params = queryParams, **lm_creds)
