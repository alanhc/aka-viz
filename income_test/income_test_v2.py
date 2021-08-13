import requests
import dateutil.parser
from datetime import timedelta, datetime

def write_csv(incomeAccount, collectDict):
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

def crawl_data(baseURL, params, collectDict, dictIdx):
    baseURL = "https://api.better-call.dev/v1/contract/mainnet/"+net_Address+"/operations"
    last_id = -1
    s = requests.Session()
    while True:
        url = baseURL
        print("proceeding...", last_id, end="\r")
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
            if(ops["destination"] != incomeAccount):
                continue
            # Parse the timestamp into datetime and transfer to UTC+8
            dt = dateutil.parser.parse( ops['timestamp'] ) + timedelta(hours=8)
            # format to yyyy-mm-dd
            dayData = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
            # Update Dictionary data
            if(collectDict.get(dayData) == None):
                collectDict[dayData][dictIdx] = ops["amount"]
            else:
                collectDict[dayData][dictIdx] += ops["amount"]
        last_id = int(r["last_id"])


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

incomeAccount = "tz1WCYsbPyHTBcnj4saWG6SRFHECCj2TTzC6"

# Market
print("Processing akaMarket...")
net_Address = "KT1HGL8vx7DP4xETVikL4LUYvFxSV19DxdFN"
params = {"entrypoints":"collect", "status":"applied"}
dictIdx = 0
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaMarket Process Done!")

# Bundle
print("Processing akaBundle...")
net_Address = "KT1NL8H5GTAWrVNbQUxxDzagRAURsdeV3Asz"
params = {"entrypoints":"collect_bundle", "status":"applied"}
dictIdx = 1
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaBundle Process Done!")

# Auction
print("Processing akaAuction [close_auction]...")
net_Address = "KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8"
params = {"entrypoints":"close_auction", "status":"applied"}
dictIdx = 2
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaGacha Process Done!")

print("Processing akaAuction [fail_close_auction]...")
net_Address = "KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8"
params = {"entrypoints":"fail_close_auction", "status":"applied"}
dictIdx = 2
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaGacha Process Done!")

print("Processing akaAuction [direct_purchase]...")
net_Address = "KT1CPzhw1UxAfdVYmeoMysVJLyA3fbvcqbi8"
params = {"entrypoints":"direct_purchase", "status":"applied"}
dictIdx = 2
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaGacha Process Done!")

# Gacha
print("Processing akaGacha...")
net_Address = "KT1P1WJuRb9K62gdx1HfkNJwohLA5EmyCoQK"
params = {"entrypoints":"oracle_gacha", "status":"applied"}
dictIdx = 3
crawl_data(net_Address, params, collectDict, dictIdx)
print("akaGacha Process Done!")
print(collectDict)

# write file
write_csv(incomeAccount, collectDict)
