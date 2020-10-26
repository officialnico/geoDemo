# Placing our bot on the same AWS data center as the exchange

You're coming so close to the exchange server that it is practically a LAN connection
this is a cutting edge advantage over every other trading bot.
Speed is of essence when making these calculation.

we'll be using Binance for this example

Most exchanges also use AWS so it's a fair bet in flexibility using this method.

#### First we ping the exchange in question to find the IP
![](https://i.ibb.co/3snmNx8/Screen-Shot-2020-10-26-at-1-19-41-PM.png)

#### Notice the location and hostname of the API server
![](https://i.ibb.co/0MjSK47/Screen-Shot-2020-10-26-at-1-19-59-PM.png)

#### This is AWS's availability zones list showing the same region as the API server uses
![](https://i.ibb.co/yhRYC7J/Screen-Shot-2020-10-26-at-1-21-57-PM.png)

#### Now we've set up an EC2 instance in that same zone
this can be done a lot more dynamically turning on or off instances in different regions depending on the exchange required by the trading bot in question.
Code concurrency can automated with Git between the instances.
Instance states can be switched on and off automatically in order to save resources and money once the bot is starting or finishing to use them.
![](https://i.ibb.co/n11ZbvQ/Screen-Shot-2020-10-26-at-1-59-58-PM.png)

#### Finally that is the location of our bot itself
as you can see it's the same one as that of the exchange's API
![](https://i.ibb.co/9HG4y93/Screen-Shot-2020-10-26-at-2-10-48-PM.png)

#### And finally the result!
![](https://i.ibb.co/zFDGFbJ/Screen-Shot-2020-10-26-at-6-32-39-PM.png)

#### Feel free to test out the difference in time on your own machines I've included everything you need in this repo
