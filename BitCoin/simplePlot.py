import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('/home/tanish/DataScience_Python_Projectcs/BitCoin/data/BTC_USD.csv')

plt.figure(figsize=(10,6))
sns.lineplot(data = df,x = 'Adj. Close', y='Volume')

plt.title('Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()
