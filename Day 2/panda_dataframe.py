
# %%
import pandas as pd
df = pd.read_csv('data\sample.csv')
# %%
colnames=df.columns.tolist()
print(colnames)
# %%
df2=df[df['age']>20]
print(df2)

# %%
