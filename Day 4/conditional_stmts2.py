#ELIF-LADDER & IF-ELSE & NESTED-IF
days=('MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY')
day=input("Enter the day:")
if day in days:
    time=int(input("Enter time:"))
    print("Available buses are:")
    if 0<=time<=6:
        print('Bus1\nBus7\nBus9')
    elif 7<=time<=13:
        print('Bus2\nBus8\nBus14')
    elif 14<=time<=21:
        print('Bus34\nBus3\nBus18')
    elif 21<=time<=23:
        print('Bus4\nBus5\nBus345')
else:
    print("Holiday, No buses are available")

#2 ELIF-LADDER
print("Welcome to Uber!")
print("1.Bike")
print("2.Auto")
print("3.Cab")

choice=int(input("Enter your preferred choice:"))

if choice==1:
    print("Selected Bike, your ride will arrive shortly")
elif choice==2:
    print("Selected Auto, your ride will arrive shortly")
elif choice==3:
    print("Selected Cab, your ride will arrive shortly")
else:
    print("Invalid Choice, Please select the listed ones")
