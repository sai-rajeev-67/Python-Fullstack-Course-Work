l=[1,2,3,4]
my_name=['sai','rajeev','lochan','medisetti']
#for list of numbers
print(l[0])
print(l[1:3])
print(l[::-1])
print(l[0:])
print(l[-1])
#membership op
print(1 in l)
print(2 not in l)
print(5 in l)

print(id(l))
l[3]=5
print(l)
print(l.append(6))#single (at the end)
print(l)
print(l.extend([7,8,9,10]))#add multiple (at the end)
print(l)
print(l.insert(0,1))#insert at certain index
print(l)
l.pop(4)
print(l)
l.remove(7)
print(l)
l.clear()
print(l)

#for list of strings

print(my_name[1])
print(my_name[0:])
print(my_name[0:3])
print(my_name[3])
print(my_name[::-1])
my_name[0]='Medisetti'
my_name.insert(1,'Sai')
my_name.insert(2,'Rajeev ')
my_name.append('Lochan')
my_name.pop(3)
my_name.remove('lochan')
my_name.remove('medisetti')
print(my_name)

my_name.clear()
print(my_name)


