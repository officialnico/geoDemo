import json
import matplotlib.pyplot as plt

def graph():
	with open('exchange_ips.json','r') as f:
		data = json.loads(f.read())


	amazon_v=0
	cloud_v=0
	others_v=0

	isps = []
	isp_set = set()
	for x in data:
		isp=data[x][1]
		isps.append(isp)
		isp_set.add(isp)

		vol = data[x][2]
		if(vol):
			if('AMAZ' in isp):
				amazon_v+=vol
			elif('CLOUD' in isp):
				cloud_v+=vol
			else:
				others_v+=vol
		else:
			vol=0



	isp_set = list(isp_set)
	isp_set_counted = []


	amazon=0
	cloud=0
	others=0


	for x in isp_set:
		if('AMAZ' in x):
			amazon += isps.count(x)
		elif('CLOUD' in x):
			cloud += isps.count(x)
		else:
			others += isps.count(x)


	#Plotting
	fig1, (ax1,ax2) = plt.subplots(1,2,figsize=(10,10))
	fig1.canvas.set_window_title("Exchange's ISP data")
	ax1.pie([amazon,cloud,others], labels=['Amazon','Cloudflare','others'], autopct='%1.1f%%',
	        shadow=True, startangle=90, colors=['red','orange','grey'])
	ax1.axis('equal')  
	title="Exchange ISP for common "+str(len(data)) +" exchanges"
	ax1.set_title(title,y=0.77)


	ax2.pie([amazon_v,cloud_v], labels=['Amazon','Cloudflare'], autopct='%1.1f%%',
	        shadow=True, startangle=90, colors=['red','orange','grey'])
	ax1.axis('equal')  
	title="Exchange ISP Total BTC/USD(T) 24hr Volumes"
	ax2.set_title(title,y=1.08)

	plt.show()

if __name__=="__main__":
	graph()
