# CAPM.py 


## Table of contents
* [About](#about)
* [Example](#example)
* [Libraries](#libraries)
* [Setup](#setup)
* [Errors](#errors)
* [Ideas](#ideas)


## About
The capital asset pricing model is a linear formula used to find the expected value of a security. 
This script performs the calculation given two parameters. A stock's ticker and the number of days
the security will be an investment. 

## Example
This example was done using python 3.8 and the spyder IDE. I also used Apple, and a duration of 900 days.

As soon as someone runs the script, they are prompted with two questions which are inputs. 
[![Screenshot-from-2020-12-25-19-24-45.png](https://i.postimg.cc/pXvwsR2G/Screenshot-from-2020-12-25-19-24-45.png)](https://postimg.cc/F1PCRtk3)

variable is the name of the object, and if we call variable.data we get all stock prices between 900 days ago
and today. (or the prices between todays date - duration and today's date)

[![Screenshot-from-2020-12-25-19-29-57.png](https://i.postimg.cc/KvVnZvRQ/Screenshot-from-2020-12-25-19-29-57.png)](https://postimg.cc/LntqDSkZ)

Inorder to get the expected value of the security we have to call variable.CAPM(), and then access the new object by
variable.E_Rt. 
[![Screenshot-from-2020-12-25-20-04-10.png](https://i.postimg.cc/FRd2fKhp/Screenshot-from-2020-12-25-20-04-10.png)](https://postimg.cc/8JGy9NJf)

Therefore, after 100 days we may expect a return of approximately 5.5% according the the CAPM. 

## Libraries 
pandas_datareader - required to access stock price data from yahoo finance. <br/>
datetime - necessary to calculate timeframe and access stock data according to that timeframe.<br/>
numpy - useful for quick computations<br/>

## Setup
pandas_datareader is a necessary library. To install from linux terminal using Anaconda:<br/>
```
$ conda activate
$ conda install -c anaconda pandas-datareader 
```
If you already have pandas_datareader then: 
```
$ git clone https://github.com/manuelnjit/CAPM.git
```

## Errors
The capitals asset pricing model is a linear formula that is used to calculate an expected value, but
stock prices are stochastic and expected values come from probability distributions. 


## Ideas
**Find the Expected Return of a Portfolio**: We could use this script to calculate expected returns for various stocks
while creating a portfolio of those stocks, and then finding the expected return of the portfolio.



