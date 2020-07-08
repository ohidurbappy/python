d={'Name':'Ohidur','Age':25,'Pro':'Coder'}

print("Name:",d['Name'])
print("Age:",d['Age'])
print('Profession:',d['Pro'])

d['Blood']='B+'

print("Blood Group:",d['Blood'])

d['Age']=26

print('New Age:',d['Age'])

print(str(d))

print(type(d)) # return type of variable

print("Length of dict:",len(d))




del d['Blood'] # remove specific key

d.clear() # remove all entries

del d # delete the dictionary



dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("New Dictionary : ",dict2)



dict3=dict.fromkeys(['name','age','city','email'])

print(dict3)

dict4=dict.fromkeys(['green','red'],10)
print(dict4)

print(dict4.get('green',100))

print(dict4.items())

print(dict3.keys())
print(dict3.values())

dict3.setdefault('age',10)