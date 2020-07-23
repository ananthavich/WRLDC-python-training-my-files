# %%
import pandas as pd
#import matplotlib.pyplot as plt
# %%
df = pd.read_excel('data/final_excel.xlsx')
# %%
#df.set_index('Date',inplace=True)
state_name=input('Enter state name :')
l=[]
colNames = df.columns.tolist()
for i in colNames:
    if i=='Date':
        continue
    elif i !=state_name:
        l.append(i) 
df.drop(l,axis=1,inplace=True)
df.plot()
# %%
