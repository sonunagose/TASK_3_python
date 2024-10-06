# clear

d1={
    "fruit":'banana',
    'color':'yellow',
    'price':'50'
}
d1.clear()
print(d1)
print()
print('-----')
print()

# Copy

d2={
     "fruit":'banana',
    'color':'yellow',
    'price':'50'
}
x=d2.copy()
print(x)
print()
print('-----')
print()

# fromkeys

a=('sheet1','sheet2','sheet3',)
b=60
thisdict=dict.fromkeys(a,b)
print(thisdict)
print()
print('-----')
print()

# get

d3={
    'a':'a1',
    'b':'b1',
    'c':'c1'
}
x=d3.get('b')
print(x)
print()
print('-----')
print()

# Items

d4 = {
    'a': 'a1',
    'b': 'b1',
    'c': 'c1'
}
x= d4.items()
print(x)
print()
print('----')
print()

# keys

d5={
     "fruit":'banana',
    'color':'yellow',
    'price':'50'
}
x=d5.keys()
print(x)
print()
print('-----')
print()

# values

d6={
     "fruit":'banana',
    'color':'yellow',
    'price':'50'
}
x=d6.values()
print(x)
print()
print('-----')
print()



# pop

d7={
    'stu':'Ojas',
    'add':'add1',
    'sub':'Science'
}
d7.pop('add')
print(d7)
print()
print('-----')
print()

# popitem

d7={
    'stu':'Ojas',
    'add':'add1',
    'sub':'Science'
}
d7.popitem()
print(d7)
print()
print('-----')
print()

# setdefault

d8={
     "fruit":'banana',
    'color':'yellow',
    'price':50
}
x=d8.setdefault('price',50)
print(x)
print()
print('-----')
print()

# update
d9={
     "fruit":'banana',
    'color':'yellow',
    'price':50
}
d9.update({'color':'green'})
print(d9)