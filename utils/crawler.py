import requests
import dateutil.parser
from datetime import timedelta, datetime

def crawl_data(jobs=[], collectDict={}, config=None) -> dict:
    s = requests.Session()
    for j in jobs:    
        url = config["Url"]["baseURL"] + config['Contract Address'][ j['contract'] ]+"/operations"
        params = j["params"]
        
        last_id = -1
        while True:
            if(last_id > 0):
                params["last_id"] = last_id
            r = s.get(url, params = params).json()
            #  Break if no operations anymore
            if(len(r["operations"]) == 0):
                print("akaMarket Process Done!")
                break
            for ops in r['operations']:
                # pass condition
                if(ops.get("parameters") != None):
                    continue
                if(ops["destination"] != config["Account"]["income"]):
                    continue
                # Parse the timestamp into datetime and transfer to UTC+8
                dt = dateutil.parser.parse( ops['timestamp'] ) + timedelta(hours=8)
                # format to yyyy-mm-dd
                dayData = str(dt.date())
                # Update Dictionary data
            
                if(collectDict.get(dayData) == None):
                    collectDict[dayData][j['dictIdx']] = ops["amount"]
                else:
                    collectDict[dayData][j['dictIdx']] += ops["amount"]
            last_id = int(r["last_id"])   
    return collectDict