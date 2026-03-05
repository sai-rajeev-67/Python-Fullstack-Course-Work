#int
a=1
print(type(a))
print(a)
print(float(a))
print(str(a))
print(bool(a))
print(complex(a))

#float
b=2.34
print(type(b))
print(b)
print(int(b))
print(str(b))
print(bool(b))
print(complex(b))

#complex
c=1+2j
print(type(c))
print(c)
print(str(c))
print(bool(c))

#str
#str conversion only works if str contains numbers
d1="234"
d="sai"
print(type(d))
print(d)
print(int(d1))#will throw error if it is mix of numbers and characters
              #(only no are allowed when converting from str to int)            
print(list(d))
print(tuple(d))
print(bool(d))


#list
#mutable
e=[1,2,3,4,5,6]
print(type(e))
print(e)
print(set(e))
print(bool(e))
print(tuple(e))


#tuple
#immutable(cannot be edited after creation)
f=(1,2,3,4,5,6)
print(type(f))
print(f)
print(set(f))
print(bool(f))
print(list(f))


#set
#no duplicates or remove duplicates
#also mutable (can be edited after creation)
g={1,2,4,5,3,4,4,4,4,4} 
print(type(g))
print(g)
print(list(g))
print(tuple(g))
print(bool(g))

#dict
#key value pair (k:v)
h={'hp':50000,'dell':45000}
print(type(h))
print(h)
print(set(h))
print(bool(h))
print(list(h))

#boolean
i=True
print(type(i))
print(i)

