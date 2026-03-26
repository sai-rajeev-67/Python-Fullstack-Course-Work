data={'123456':{ 'pin': '1234', 'balance':4000, 'history' :[]},
      '234561':{ 'pin': '1234', 'balance':5000, 'history' :[]},
      '345612':{ 'pin': '1234', 'balance':7000, 'history' :[]},
      '456123':{ 'pin': '1234', 'balance':9000, 'history' :[]}
}


def deposit(acc_num):
    print("-----------------------------------------------")
    amount=int(input("Enter the amount:"))
    data[acc_num]['balance']+= amount
    print(f"{amount} is deposited succesfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount} is deposited")
    print("-----------------------------------------------")
def withdraw(acc_num):
    print("-----------------------------------------------")
    amount=int(input("Enter the amount:"))
    if amount <= data[acc_num]['balance']:
        data[acc_num]['balance']-= amount
        print(f"{amount} is withdrawed succesfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount} is withdrawed")
    print("-----------------------------------------------")
def change_pin(acc_num):
    print("-----------------------------------------------")
    new_pin=input("Enter new pin:")
    data[acc_num]['pin']= new_pin
    print("pin is changed")
    data[acc_num]['history'].append("pin is changed")
    print("-----------------------------------------------")
def check_balance(acc_num):
    print("Current Balance is:",data[acc_num]['balance'])
def view_transactions(acc_num):
    print("Transactions are:", data[acc_num]['history'])
def menu():
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[H]istory")
    print("Change[P]in")
    print("[E]xit")


print("---------------Welcome To ATM-------------------")
acc_num=input("Enter The Account number:")
pin=(input("Enter The Pin:"))
if acc_num in data and data[acc_num]['pin']== pin:
    print("Login Succesful")
    while True:
        menu()
        ch=input("Enter your choice:").lower()
        if ch=='c':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='h':
            view_transactions(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("------------------Thank You-------------------")
            break
        else:
            print("Enter a valid choice")
else:
    print("Invalid Login")
