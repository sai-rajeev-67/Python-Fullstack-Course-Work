#recursion : A function which calls itself
#
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
    
display(1)


print("-------------------------------------------------")

#2ND CODE 10 to n integers
def display2(n):
     if n<=0:
        return
    print(n)
    display2(n-1)
    
display2(10)

print("-------------------------------------------------")

#3rd both in one

def display(n):
    if n>10:
        return
    print("Before:",n)
    display(n+1)

    print("After:",n)
display(1)



