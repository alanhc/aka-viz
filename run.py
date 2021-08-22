from utils.crawler import *
from datetime import timedelta, datetime
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')
##### Config #####
beginTime = datetime(2021, 7, 10).date() 
contracts = config.items("Contract Address")
jobs = [
    {"contract":"market", "dictIdx":0, "params":{"entrypoints":"collect", "status":"applied"} },
    {"contract":"bundle", "dictIdx":1, "params":{"entrypoints":"collect_bundle", "status":"applied"} },
    {"contract":"auction", "dictIdx":2, "params":{"entrypoints":"close_auction", "status":"applied"} },
    {"contract":"auction", "dictIdx":2, "params":{"entrypoints":"fail_close_auction", "status":"applied"} },
    {"contract":"auction", "dictIdx":2, "params":{"entrypoints":"direct_purchase", "status":"applied"} },
    {"contract":"gacha", "dictIdx":3, "params":{"entrypoints":"oracle_gacha", "status":"applied"} },
]
##### Config #####

collectDict = {}
now = beginTime
while (datetime.now().date()-now > timedelta(days=0)):
    collectDict[str(now)] = [0] * len(contracts)
    now+=timedelta(days=1)

collectDict = crawl_data(jobs=jobs, collectDict=collectDict, config=config)
df = pd.DataFrame.from_dict(collectDict, orient='index', columns=["market","bundle","auction","gacha"])
df.to_csv("data/income_"+config["Account"]["income"]+"("+str(beginTime)+"_"+str(datetime.now().date())+").csv")
