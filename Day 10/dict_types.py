d=56

type(d)
data={'name':'sai','age':'21', 'course':'pfs','skills':['python','sql','plsql']}
print(data)
#accesing the value by using key
print(data['name'])

#modifying the value by using key
data['name']='rajeev'
print(data['name'])

# adding new key,value at the end 
data['id']=2026
print(data)

data[d]='5000'
print(data)

# adding multiple key , value pairs
data.update({1: 25, 1.1 :46})
print(data)

# deleting the items
del data[ 1]
print(data)

#deleting using popitems

data.popitem()
print(data)
#deleting using pop, removes certain items

data.pop('id')
print(data)

data.pop(56)
print(data)
# methods in a dictionary

print(data.items())  # prints key,values in list of tuples

print(data.values())  #prints values

print(data.keys())  # prints keys

print(sorted(data)) #prints sorted keys

print(min(data))

print(max(data))

print(len(data))


