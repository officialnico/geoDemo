#Will go through every exchange in the CCXT list which includes most popular exchanges and find their IP and corresponding ISP

import ccxt
import socket
from ipwhois import IPWhois
from pprint import pprint
import json
import time

def get_ip(exchange_obj):
    ip = False
    api_url = exchange_obj.urls['api']
    api_urls = api_url
    for x in api_url:
        if(isinstance(api_url,  str)): break
        api_url = api_url[x]
    api_url=api_url[8:]
    if('/' in api_url): api_url=api_url[:api_url.index('/')]
    try:
        if('hostname' in api_url): return False
        ip = socket.gethostbyname(api_url)
    except Exception as e:
        return False
    return ip

def get_all_ips():
    ips={}
    for ex in ccxt.exchanges:
        exchange = getattr(ccxt, ex)({'enableRateLimit': True})  # 'verbose': True
        ip = get_ip(exchange)
        if(not ip): continue
        isp = get_country(ip)
        ips[str(exchange)]=[str(ip),str(isp),get_volume(exchange)]
        print(ex,ips[str(exchange)])
        time.sleep(0.1)

    if(input('save y/n?')=='y'):
        save(ips)

def save(dic_data):
    with open('exchange_ips.json','w') as outfile:
            json.dump(dic_data, outfile)

def get_country(ip):
    ip_dict = IPWhois(ip).lookup_rdap()
    return ip_dict['entities'][0]

def get_volume(exchange):
    ret = None
    try:
        ret = exchange.fetchOHLCV("BTC/USDT", timeframe='1d',limit=1)[0][5]
    except:
        pass
    if(not ret):
        try:
            ret = exchange.fetchOHLCV("BTC/USD", timeframe='1d',limit=1)[0][5]
        except: 
            pass
    return ret

get_all_ips()

# b=ccxt.binance()
# print(get_volume(b))
