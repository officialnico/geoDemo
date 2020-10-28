import ccxt
import time
import os

#Checking key permission
if(os.access('tokyo_test.pem', os.W_OK)):
    os.system("chmod 400 tokyo_test.pem")

#Code on Tokyo server
binance = ccxt.binance({'apiKey':'JIgMetKmXC4ce9fnzbCznNfML7KN5SXccnxFi69JP7CnCKHUAQAOpOo4M8etyIBL','secret':'ieD0IvEtAzhHYA6ncgCce5Wog6RSFaNt8KqrLWuMGux8rClaPMsua5ELVACRjHWj'})
t1 = time.time()
balance = binance.fetchBalance()
speed_here = time.time()-t1

cmd = """ssh -i 'tokyo_test.pem' ec2-user@ec2-3-112-93-225.ap-northeast-1.compute.amazonaws.com python3.8 speed_test.py"""
speed_tokyo = float(os.popen(cmd).read())

print("""request type: fetchBalance""")
print("current location:", speed_here)
print("server at AWS location of exchange:", speed_tokyo)
print("request time difference:", int((speed_here-speed_tokyo)/(speed_tokyo)*100),'%')
