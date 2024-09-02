import pandas as pd

def getCurrencyData(currency):

    FxDataframe = pd.read_csv("TRADE WEIGHTED AVERAGE INDICATIVE RATES.csv")

    Currencydataframe = FxDataframe[FxDataframe["Currency"] == currency]

    return Currencydataframe

#ask for user input
currency = input("Enter the currency that exchanges with the Kenyan Shilling: ")
print(getCurrencyData(currency))