import pandas as pd
import yfinance as yf
import numpy as np
from prophet import Prophet


#create a class for the time series pipeline
class AdvancedTimeSeriesForecaster:  #class for the time series forecaster

    def __init__(self):
        self.forecast = {}
    
    def get_data(self, ticker:str, period:str):

        stocks = yf.Ticker(ticker)
        data = stocks.history(period=period)






        return data #results