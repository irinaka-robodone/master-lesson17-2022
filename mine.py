import json
import requests
import pprint

def station(keido,ido):
    api = "http://express.heartrails.com/api/json?method=getStations&x={x},&y={y}"
    url = api.format(x=keido,y=ido) 

    ret = requests.get(url)
    ret_json = json.loads(ret.text)
    pprint .pprint(ret_json)

keido=input("経度:")
ido=input("緯度:")

station(keido,ido)
