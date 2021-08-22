import requests
import dateutil.parser
from datetime import datetime

daoTokenUrl="https://api.better-call.dev/v1/contract/mainnet/KT1AM3PV1cwmGRw28DVTgsjjsjHvmL6z4rGh/operations"

def getDAOTokenAssignment(beginTime: datetime,endTime: datetime) -> dict[str,int]:
    record = dict()
    btimestamp = str(int(beginTime.timestamp() * 1000))
    etimestamp = str(int(endTime.timestamp() * 1000)) 
    reqParam = {'entrypoints':'transfer','from':btimestamp,'to':etimestamp,'status':'applied'}
      
    while True:
        resp=requests.get(daoTokenUrl,params=reqParam)
        #print("Req send") 
        #print (resp.url)
        if (resp.ok):

            dat = resp.json()
            opers = dat['operations']
            if(len(opers)==0):
                break
            opers = [x for x in opers if x['source']=="KT1QjeN8mDVWX4xpPVioGKBhBJFiMeT2pDof" and x['destination']=="KT1AM3PV1cwmGRw28DVTgsjjsjHvmL6z4rGh"]
            for op in opers:
                txs = op['parameters'][0]['children'][0]['children'][1]['children'][0]['children'];
                #print(txs)
                des_addr = txs[0]['value']
                amt = int(txs[2]['value'])
                record[des_addr]=record.get(des_addr,0)+amt
            last_id =int( dat['last_id'])
            reqParam['last_id']=str(last_id)
        else:
            print (resp.raise_for_status())
        

    return record
if __name__ == "__main__":
    print (getDAOTokenAssignment(dateutil.parser.parse("20210804"),dateutil.parser.parse('20210805')))
