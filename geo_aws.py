import ccxt
import time
import os
import config

def geo_aws():
	#Checking key permission
	if(os.access('tokyo_test.pem', os.W_OK)):
	    os.system("chmod 400 tokyo_test.pem")
	if(os.access('sf_key.pem', os.W_OK)):
	     os.system("chmod 400 sf_key.pem")

	#Code on Tokyo server
	#This is a testing binance account
	binance = ccxt.binance({'apiKey':config.apiKey,'secret':config.secret})
	t1 = time.time()
	balance = binance.fetchBalance()
	speed_here = time.time()-t1

	cmd = """ssh -i 'tokyo_test.pem' ec2-user@ec2-3-112-93-225.ap-northeast-1.compute.amazonaws.com python3.8 speed_test.py"""
	speed_tokyo = float(os.popen(cmd).read())

	print("--AWS--")
	print("Exchange: Binance\nAPI Location: AWS Tokyo")
	print("""request type: fetchBalance (Private API)""")
	print("current location:", speed_here)
	print("server at AWS location of exchange (Tokyo):", speed_tokyo)
	print("request time difference:", int((speed_here-speed_tokyo)/(speed_tokyo)*100),'%')
	sf_speed_test()

def sf_speed_test():
	kraken = ccxt.kraken()
	t1 = time.time()
	book = kraken.fetchTicker("BTC/USDT")
	speed_here = time.time()-t1

	cmd = """ssh -i 'sf_key.pem' ec2-user@ec2-52-53-242-202.us-west-1.compute.amazonaws.com python3.8 speed_test.py"""
	speed_sf = float(os.popen(cmd).read())
	print("\n--CloudFlare--")
	print("Exchange: Kraken\nAPI Location: CloudFlare SF")
	print("""request type: fetchTicker (Public API)""")
	print("current location:", speed_here)
	print("server at AWS location of exchange (SF):", speed_sf)
	percentage = int((speed_here-speed_sf)/(speed_sf)*100)
	print("request time difference:", percentage,'%')

	if(percentage<60 and input('rerun? y/n')=='y'):
		sf_speed_test()
		time.sleep(1)
		sf_speed_test()

if __name__=="__main__":
	geo_aws()
