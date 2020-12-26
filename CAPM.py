#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:54:15 2020

@author: stochasticity
"""
from pandas_datareader import data
from datetime import date, timedelta
import numpy as np



# This script was influenced by the Capital Asset Pricing Model 

stock_initial = input("Please enter ticker name of stock: ")

# duration_initial should be an integer. For example the number 90
# would indicate that the investment will be for atleast 90 days

duration_initial = input("Please enter duration of investment in days: ")

class CAPM:
    def __init__(self,stock, period):
        self.stock = stock   # creating stock object to acces stock ticker
        self.period = period # creating period object to access duration
        
    
        def pan_dataread(stock, period): # method to pull stock data from 
                                         # Yahoo Finance
            self.data = data.DataReader(stock, data_source='yahoo',   
                        start=date.today()-timedelta(days=int(period)),            
                        end=date.today().strftime("%Y-%m-%d"))['Adj Close']
        pan_dataread(self.stock, self.period) # creating data object contains
                                              # stock prices for use
    
    def CAPM(self):                      # Capital Asset Pricing Model 
                                         # Ross, Westerfield, Jaffe, Jordan
        rf = 0.07 # 2 Month Treasury Yield Curve Rate
        # using S&P 500 index as market
        market = data.DataReader('^GSPC', data_source='yahoo',   
                        start=date.today()-timedelta(days=int(self.period)),            
                        end=date.today().strftime("%Y-%m-%d"))['Adj Close']
        market_chg = market.pct_change().dropna() # stock prices in daily 
                                                  # daily returns
        market_sigsq = np.var(market_chg)         # S&P volatiltiy
        cov_ = np.cov(self.data.pct_change().dropna().values,
                      market_chg.values)          # covariance between S&P and
                                                  # chosen stock
                                                  
        Beta = cov_[0][1]/market_sigsq   # covariance/market variance
        expected_rm = np.mean(market_chg)# expected market return
        
        self.E_Rt = rf + Beta*(expected_rm-rf) # expected security return
        
variable = CAPM(stock_initial, duration_initial)