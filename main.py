
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

#Extra Modul für die Weltbank Daten
import pandas_datareader.wb as wb

#um Log return berechnen
import numpy as np



#import gold prices
gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)

#import crude oil prce
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

#Start und Endvariabeln erstellen
start = datetime(1999,1,1)
end = datetime(2019,1,1)

#import Nasdaq 100 prices from FRED API
nasdaq_data = web.DataReader('NASDAQ100','fred',start,end)
print(nasdaq_data)

#import S&P 500 data via FRED API
sap_data = web.DataReader('SP500','fred',start,end)
print(sap_data)

#Download der Daten mithilfe der wb.download Funktion, NY.GDP.MKTP.CD = Datenindikator
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD',country= ['US'],start=start,end=end)
print(gdp_data)

#API World Bank daten für Export Daten Gods and Services
export_data = wb.download(indicator='NE.EXP.GNFS.CN',country= ['US'],start=start,end=end)
print(gdp_data)
print(export_data)

#log return berechnen
def log_return(prices):
  lg_return = np.log(prices/prices.shift(1))
  return lg_return

#rendite Goldpreis berechnen
gold_returns = log_return(gold_prices['Gold_Price'])
print(gold_returns)

crudeoil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
print(crudeoil_returns)

sap_returns = log_return(sap_data['SP500'])
print(sap_returns)

nasdaq_data = log_return(nasdaq_data['NASDAQ100'])
print(nasdaq_data)

gdp_data = log_return(gdp_data['NY.GDP.MKTP.CD'])
print(gdp_data)

export_data = log_return(export_data['NE.EXP.GNFS.CN'])
print(export_data)

#Varianz berechnen
print(gold_returns.var())
print(crudeoil_returns.var())
print(sap_returns.var())
print(nasdaq_data.var())
print(gdp_data.var())
print(export_data.var())

