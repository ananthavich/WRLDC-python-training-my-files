# %%
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# %%
df = pd.read_excel('data/final_excel.xlsx')
# %% To convert date into string and remove time stamp
datealone_string=[]
for i in range(df.shape[0]):
   datealone_string.append(str((df['Date'].iloc[i]).date()))
df['Date']=datealone_string
# %% To modify dataframe as per user input
date=str(input('Input date in (yyyy-mm-dd) :'))
df3=df[ (df['Date']==date) ]     
state_name=input('Enter state name :')
df3=df3[['Block number',state_name]]
start_block=int(input('Enter starting block :'))
end_block=int(input('Enter ending block  :'))
df3=df3[(df3['Block number']>=start_block) & (df['Block number']<=end_block) ]
# %% All plotting functions on final dataframe obtained
def plotfunc():  
   fig, ax = plt.subplots()
   la, = ax.plot(df3['Block number'],df3[state_name])
   ax.set_title('Load Vs Time block')
   ax.set_xlabel("Block number")
   ax.set_ylabel(state_name)
   plt.show()
plotfunc()
# %%
