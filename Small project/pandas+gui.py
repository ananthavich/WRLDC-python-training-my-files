# %%
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# %%
df = pd.read_excel('data/final_excel.xlsx')
# %% To convert date into string and remove time stamp
datealone_string=[]
for i in range(df.shape[0]):
   datealone_string.append(str((df['Date'].iloc[i]).date()))
df['Date']=datealone_string
# %%
uniq_dates_list=df['Date'].unique().tolist()
state_list=df.columns.values.tolist()
del state_list[0:2]
# %%
data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df2 = pd.DataFrame(data1,columns=['Country','GDP_Per_Capita'])
# %%
window=Tk()
window.title('DataPlotter')
window.geometry("1000x3000+10+10")
lbl=Label(window, text="Select State and Date and press ok", fg='Red', font=("Helvetica", 12))
lbl.place(x=60, y=100)
cb1=Combobox(window)
cb1['values']=state_list
cb1.place(x=60, y=125)
cb2=Combobox(window)
cb2['values']=uniq_dates_list
cb2.place(x=300, y=125)
def checkcb():
    state_name=cb1.get()
    date=cb2.get()
    plotfunc(state_name,date)
def plotfunc(state_name,date):  
    df1=df[ (df['Date']==date) ]
    figure = plt.Figure(figsize=(5,4), dpi=100)
    figure.add_subplot(111).plot(df1['Block number'],df1[state_name])
    chart= FigureCanvasTkAgg(figure, window)
    chart.get_tk_widget().place(x=60, y=200)
btn = Button(window, text="Ok",command=checkcb)
btn.place(x=500,y=122)
window.mainloop()
# %%
