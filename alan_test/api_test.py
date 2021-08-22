import requests
import dateutil.parser
from datetime import timedelta
import pandas as pd
def crawl_data():
    net_Address = "KT1HGL8vx7DP4xETVikL4LUYvFxSV19DxdFN"
    params = {"entrypoints":"collect"}
    baseURL = "https://api.better-call.dev/v1/contract/mainnet/"+net_Address+"/operations"
    last_id = -1
    collectDict = {}
    s = requests.Session()
    while True:
        url = baseURL
        print("proceeding...", last_id, end="\r")
        if(last_id > 0):
            params["last_id"] = last_id
        
        r = s.get(url, params = params).json()
        if (len(r["operations"])==0):
            print("Done.")
            break
        for ops in r['operations']:
            # pass condition #
            if(ops.get("parameters") == None):
                continue
            if(ops["parameters"][0]["name"] != "collect"):
                continue
            # pass condition #
            # Parse the timestamp into datetime and transfer to UTC+8
            dt = dateutil.parser.parse( ops['timestamp'] ) + timedelta(hours=8)
            # format to yyyy-mm-dd
            dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
            # Update Dictionary data
            if(collectDict.get(dayData) == None):
                collectDict[dayData] = ops["amount"]
            else:
                collectDict[dayData] += ops["amount"]
        last_id = int(r["last_id"])
    df = pd.DataFrame(collectDict.items(), columns=["Date", "Amount"])
    print(df)
    df.to_csv("data.csv")

#crawl_data()