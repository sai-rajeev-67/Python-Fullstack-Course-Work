#1st give each character in a new line
def display(n):
    for i in n:
        print(i)
display("python")
print("------------------------------------------------")


#2nd strip characters 

def display(s,i):
    if i==len(s):
        return
    print(s[i])
    display(s,i+1)
display("python",0)

print("------------------------------------------------")
#3rd reverse order of characters

def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[i])
    
display("python",0)

print("------------------------------------------------")

#4th print p py pyt pyth pytho python

def display(s,i):
    if i==len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("python",0)

print("------------------------------------------------")

#5th prints python pytho pyth pyt py p

def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[:i+1])
display("python",0)

print("------------------------------------------------")

#6th print ab abab ababab

def display(s,i):
    if i==0:
        return
    display(s,i-1)
    print(s*i)
display("abc",6)

print("------------------------------------------------")

#7th reverse order ababab abab ab

def display(s,i):
    if i==0:
        return
    print(s*i)
    display(s,i-1)
display("abc",6)

print("------------------------------------------------")

#8th

def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("rajeev",0,3)
print("------------------------------------------------")
#9th sum of elements in a list

def display(l):
    s=0
    for i in l:
        s+=i
    return s
print("Sum of ele in list is:",display([1,2,3,4,5]))

print("------------------------------------------------")

#10th same but recursive

def display(l,i,s):
    if i==len(l):
        return s
    return display(l,i+1,s+l[i])
print(display([1,2,3,4,5],0,0))

print("------------------------------------------------")

##11th using strings in list

def display(l):
    r=""
    for i in l:
        r+=i
    print(r)
display(["Sai","Rajeev"])

print("------------------------------------------------")

    
#12th same but recursive
def display(l,i,s):
    if i==len(l):
        return s
    return display(l,i+1,s+l[i])
print(display(['sai','Rajeev'],0,''))
