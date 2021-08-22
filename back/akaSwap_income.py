import requests
import dateutil.parser
from datetime import timedelta, datetime

incomeAccount = "tz1WCYsbPyHTBcnj4saWG6SRFHECCj2TTzC6"

startTime = datetime.strptime('10 Jul 2021', '%d %b %Y').date()
endTime = (datetime.now() + timedelta(hours=8)).date()

currentDay = startTime
collectDict = {}
while True:
    # market, bundle, auction, gacha
    arr = [0, 0, 0, 0]
    dayData = str(currentDay.year) + "-" + str(currentDay.month) + "-" + str(currentDay.day)
    collectDict[dayData] = arr
    currentDay = currentDay + timedelta(days=1)
    if (currentDay > endTime):
        break


# Market

print("Processing akaMarket...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1HGL8vx7DP4xETVikL4LUYvFxSV19DxdFN/operations?status=applied&entrypoints=collect"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaMarket Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][0] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])


# Bundle

print("Processing akaBundle...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1NL8H5GTAWrVNbQUxxDzagRAURsdeV3Asz/operations?status=applied&entrypoints=collect_bundle"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaBundle Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][1] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])


# Auction

print("Processing akaAuction [close_auction]...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8/operations?status=applied&entrypoints=close_auction"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaGacha Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][2] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])



print("Processing akaAuction [fail_close_auction]...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8/operations?status=applied&entrypoints=fail_close_auction"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaGacha Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][2] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])


print("Processing akaAuction [direct_purchase]...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8/operations?status=applied&entrypoints=direct_purchase"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaGacha Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][2] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])




# Gacha

print("Processing akaGacha...")

baseURL = "https://api.better-call.dev/v1/contract/mainnet/KT1P1WJuRb9K62gdx1HfkNJwohLA5EmyCoQK/operations?status=applied&entrypoints=oracle_gacha"
last_id = -1

while True:
    url = baseURL
    if(last_id > 0):
        url += "&last_id=" + str(last_id)
    r = requests.get(url).json()

    print("Get " + str(len(r["operations"])) + " datas.")
    #  Break if no operations anymore
    if(len(r["operations"]) == 0):
        print("akaGacha Process Done!")
        break
    for idx in range(len(r["operations"])):
        # print("Idx : " + str(idx))
        if(r["operations"][idx].get("parameters") != None):
            continue
        if(r["operations"][idx]["destination"] != incomeAccount):
            continue
        # Get Timestamp UTC+0
        timestamp = r["operations"][idx]["timestamp"]
        # Parse the timestamp into datetime and transfer to UTC+8
        dt = dateutil.parser.parse(timestamp) + timedelta(hours=8)
        # format to yyyy-mm-dd
        dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        # Update Dictionary data
        collectDict[dayData][3] += r["operations"][idx]["amount"]

    # Update the next last_id
    last_id = int(r["last_id"])


print(collectDict)

csvPath = './Income_'+incomeAccount+'.csv'
f = open(csvPath, 'w')
f.write('Date, market, bundle, auction, gacha, total\n')

currentDay = startTime
totalPrice = [0, 0, 0, 0, 0]
while True:
    # market, bundle, auction, gacha
    dayData = str(currentDay.year) + "-" + str(currentDay.month) + "-" + str(currentDay.day)
    dailyTotalPrice = 0
    for i in range(4):
        totalPrice[i] += collectDict[dayData][i]
        dailyTotalPrice += collectDict[dayData][i]
    totalPrice[4] += dailyTotalPrice
    fileData = dayData + "," + str(collectDict[dayData][0]) + "," + str(collectDict[dayData][1]) + "," + str(collectDict[dayData][2]) + "," + str(collectDict[dayData][3]) + "," + str(dailyTotalPrice) + "\n"
    f.write(fileData)
    currentDay = currentDay + timedelta(days=1)
    if (currentDay > endTime):
        break

fileData = "Total," + str(totalPrice[0]) + "," + str(totalPrice[1]) + "," + str(totalPrice[2]) + "," + str(totalPrice[3]) + "," + str(totalPrice[4])
f.write(fileData)
f.close()