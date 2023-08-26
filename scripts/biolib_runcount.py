# run with 
# BIOLIB_TOKEN=<BIOLIB_TOKEN> python scripts/biolib_runcount.py

import biolib

biolib.sign_in()
p=biolib.api.client
pp=p.get(url='/apps/',params={'account_handle':'YaoYinYing','app_name':'pprcode'})
print(pp.json()['results'][0]['job_count'])