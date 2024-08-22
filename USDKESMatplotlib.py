import numpy as np
import pandas
import matplotlib

def generateNewChart(csv):
    data = pandas.DataFrame(csv)
    print(data)

generateNewChart("TRADE WEIGHTED AVERAGE INDICTIVE RATES.csv")
