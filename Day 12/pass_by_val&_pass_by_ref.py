#int
def display(n):
    n+=10
    print("Inside:",n)

n=10
display(n)
print("Outside:",n)

print("---------------------------------------------")

#float
def display(n):
    n+=10
    print("Inside:",n)

n=10.34
display(n)
print("Outside:",n)

print("---------------------------------------------")

#str
def display(n):
    n+="M"
    print("Inside:",n)

n="Sai"
display(n)
print("Outside:",n)

print("---------------------------------------------")

#list

def display(n):
    n+=[6,7]
    print("Inside:",n)

n=[1,3,4]
display(n)
print("Outside:",n)

print("---------------------------------------------")

def display(n):
    n.extend([6,7])
    print("Inside:",n)

n=[1,3,4]
display(n)
print("Outside:",n)

print("---------------------------------------------")

#dict
def display(n):
    n[7]= 8
    print("Inside:",n)

n={1:3,4:6}
display(n)
print("Outside:",n)
