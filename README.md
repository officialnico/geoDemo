The idea here is to place our trading scripts on the same AWS platform as the exchange
Since AWS also uses their own DNS you're coming to so close to the exchange server that it is practically a LAN connection
Most exchanges also use AWS so it's a fair bet in flexibility using this method.

we'll be using Binance for this example

##### First we ping the exchange in question to find the IP
![](https://i.ibb.co/3snmNx8/Screen-Shot-2020-10-26-at-1-19-41-PM.png)

##### Notice the location and hostname of the API server
![](https://i.ibb.co/0MjSK47/Screen-Shot-2020-10-26-at-1-19-59-PM.png)

##### This is AWS's availability zones list showing the same region as the API server uses
![](https://i.ibb.co/yhRYC7J/Screen-Shot-2020-10-26-at-1-21-57-PM.png)

##### Now we've set up an EC2 instance in that same zone
this can be done a lot more dynamically turning on or off instances in different regions depending on the exchange required by the trading bot in question.
Code concurrency can automated with Git between the instances.
Instance states can be switched on and off automatically in order to save resources and money once the bot is starting or finishing to use them.
![](https://i.ibb.co/n11ZbvQ/Screen-Shot-2020-10-26-at-1-59-58-PM.png)

##### Finally that is the location of our bot itself
as you can see it's the same one as that of the exchange's API
![](https://i.ibb.co/9HG4y93/Screen-Shot-2020-10-26-at-2-10-48-PM.png)

