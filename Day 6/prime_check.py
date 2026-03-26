def prime_check(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    return False
n= int(input())
list_prime = []

for i in range(2,n+1):
    if prime_check(i) == True:
        list_prime.append(i)

if n in list_prime:
    ind = list_prime.index(n) + 1
    print(ind)
else:
    print("Not a prime")
