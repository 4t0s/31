import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  datetime

data = pd.read_csv("efirium_quotes.csv", sep=";")
print(data['average'])
print(data['high'])

plt.plot(data['updated'], data['average'], data['high'], data['low'])
plt.show()
plt.ion(data['updated'], data['volume'])
plt.show()