import ccxt
import time
import pprint
import os
import json
import graph_isp
import geo_aws

input("\nWhen creating trading bots request time is what separated you from the losing bots\n")
input("As we need flexibility for what exchange we are using we need to make sure our geolocation optimatimization works flexible\nto the location of exchange servers\n")
prompt="Here we have a list of 104 of the most common exchanges including all the relevant ones like binance, kraken, bitfinex, etc\n"
input(prompt)


for ex in ccxt.exchanges:
	print('\t',ex)
	time.sleep(0.02)

input("")

input("\nWhat really matters here? lets take a look at who their ISP's are to find an appropriate location\n")

with open('exchange_ips.json','r') as f:
	data = json.loads(f.read())

for x in data:
	print('\t',x,data[x][0],data[x][1])
	time.sleep(0.02)

input("\nThis is lots of information... Lets graph it!")
graph_isp.graph()

input("\nSo for the real test ive set up a couple test servers one in Tokyo in the same AWS facility as Binance!!\n")

input("I've also set one up down the street from cloudflare at the SF AWS location giving us CloudFlare GeoLocation optimization as well as maintaining unison with the AWS API")

input("\nLet's see some results\n")

geo_aws.geo_aws()


# os.system(gra)