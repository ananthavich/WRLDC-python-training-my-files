
#%%
x=8
type(x)


# %%
x= {
    'firstname':'Anantha',
    'lastname':'krishnan',
    'age':26,
    'address':{'home':'aparna',
               'city':'alappuzha',
               'state':'kerala'
            }
}
print(type(x))

# %%
isNum=isinstance(x,dict)
print(isNum)

# %%
xkeys=list(x.keys())#access all keys of dictionary
print('keys of dictionary x is',xkeys)
# %%
xvals=list(x.values())#access all keys of dictionary
print('values of dictionary x is',xvals)
# %%
typesarr=[type(i) for i in xvals]
print(typesarr)

# %%
x['age']='27'

# %%
print("{0} {1} aged {2} lives in {3}".format(x['firstname'],x['lastname'],x['age'],x.['address'].join()) )


# %%


# %%
