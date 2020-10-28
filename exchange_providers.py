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
        print(exchange,ip, isp)
        ips[str(exchange)]=[str(ip),str(isp)]
        time.sleep(0.1)

    if(input('save y/n?')=='y'):
        save(ips)

def save(dic_data):
    with open('exchange_ips.json','w') as outfile:
            json.dump(dic_data, outfile)

def get_country(ip):
    ip_dict = IPWhois(ip).lookup_rdap()
    return ip_dict['entities'][0]


get_all_ips()
