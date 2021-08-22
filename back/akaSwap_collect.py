import requests
import dateutil.parser
from datetime import timedelta

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1HGL8vx7DP4xETVikL4LUYvFxSV19DxdFN/operations?entrypoints=collect"

collectDict = {}
last_id = -1
while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()
    print(last_id)
    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") == None):
            continue
        if(r["operations"][idx]["parameters"][0]["name"] != "collect"):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        if(collectDict.get(dayData) == None):
            collectDict[dayData] = r["operations"][idx]["amount"]
        else:
            collectDict[dayData] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])

print(collectDict)

