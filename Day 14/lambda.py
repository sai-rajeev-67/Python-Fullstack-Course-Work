from functools import reduce
#1st 
def wish(name):
    return f"Hello {name} , Welcome to the class"
wish1= lambda name: f"Hello {name} , Welcome to the class"

print(wish("Sai"))
print(wish("Adi"))

print("------------------------------------------------------------------------")
#2nd

def add(a,b,c):
    return (a+b+c)/3
add= lambda a,b,c : (a+b+c)/3

print(add(2,3,99))
print((add(134,143,1432)))
print(round(add(2,3,99)))
print(round(add(134,143,1432)))

print("------------------------------------------------------------------------")


#3rd

def iseven(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

iseven1= lambda n : "Even" if n%2==0 else "odd"

print(iseven(14))
print(iseven1(1567))

print("------------------------------------------------------------------------")

#4th

def isgreater(a,b):
    if a>b:
        return f"{a} is bigger"
    else:
        return f"{b} is bigger"

isgreater1= lambda a,b: f"{a} is bigger" if a>b else f"{b} is bigger"

print(isgreater1(235,123))

print("------------------------------------------------------------------------")

# 5th

def isVowel(s):
    vol='aeiouAEIOU'
    if s in vol:
        return "Vowel"
    else:
        return "Consonant"
vol='aeiouAEIOU'
isVowel1= lambda s: "vowel" if s in vol else "consonant"

print(isVowel("i"))
print(isVowel1("a"))

print("------------------------------------------------------------------------")

#6th

def list_incr(l):
    for i in range(len(l)):
        l[i]= l[i]+10
    return l

def list_check(l):
    res=[]
    for i in range(len(l)):
        if l[i]%3==0:
            res.append(l[i])
    return res

l=[10,20,30,40]

list_incr1= list(map(lambda i:i+10, l))
list_incr2= list(map(lambda i: f"${i} .00", l))
list_incr3= list(map(lambda i: i+i*0.18, l))
res = list(filter(lambda i: i%3==0, l))

           
print(list_incr(l))
print(list_incr1)
print(list_incr2)
print(list_incr3)
print(res)



print("------------------------------------------------------------------------")

#7th

L1=[100,20,60,200,345,76,23,34,45]
greater_than_60= list(filter(lambda i: i>60 ,L1))
print(greater_than_60)

print("------------------------------------------------------------------------")

#8th
d={'laptop': True, 'phone': True, 'Mouse': True, 'Charger':True, 'Tablet':False}
isthere=list(filter(lambda i:d[i],d))
print(isthere)

print("------------------------------------------------------------------------")

#9th

l3=[1,2,3,4,5,6,7,8,9,10,11,12]
iseven=list(filter(lambda i: i%2==0, l3))
print(iseven)
print("------------------------------------------------------------------------")

#10TH

l4=[10,22,3,4,5,6,7,8,4,222,33,4]
sumofall=reduce(lambda a,b: a+b, l4)
print(sumofall)
print("------------------------------------------------------------------------")

#11th

s7=['Sai','Rajeev','Lochan']
addcharsinsidelist= reduce(lambda a,b:a+''+b,s7)
print(addcharsinsidelist)
print("------------------------------------------------------------------------")

#12th

d1={'laptop': 50000, 'phone': 20000, 'Mouse': 500, 'Charger':3000, 'Tablet':7000}

print(dict(sorted(d1.items())))



