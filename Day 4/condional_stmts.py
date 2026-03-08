#SIMPLE IF
print('Simple if')
a=int(input())
if a>0:
    print(f"{a} is a positive number")
#IF-ELSE

m=int(input())
if m>35:
    print(f"Student got {m} marks, so he passed the exam")
else:
    print(f"Student got {m} marks, so he failed the exam")

#ELIF-LADDER & NESTED IF

seat_type=('Gold','Bronze','Recliners')
seat=input()
if seat in seat_type: 
    if seat=='Gold':
        print('200 rs')
    elif seat=='Bronze':
        print('100 rs')
    elif seat=='Recliners':
        print('300 rs')
else:
    print('Seat not found! please try again')

          
