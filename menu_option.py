from main import *

accountnumber = 0


def login_menu():
    global accountnumber
    next_state = ""
    print("\nWelcome to the bank system. Please enter your account number and pin.\n")
    accountnumber = int(input("Account number? "))
    pin = int(input("PIN? "))

    db_pin = get_pin(accountnumber)

    if (pin == db_pin):
        print("\nYou have logged in successfuilly")
        next_state= 'standard_menu'
    else:
        input("PIN nummber is incorrect. Try again: ")
        next_state= 'login_menu'

    return next_state

def standard_menu():
    options = {"a":"check_balance_menu","b":"withdraw_menu", "c":"deposit_menu","q":"quit"}
    
    print("\nselect your options")
    print("a - Check Balance")
    print("b - Withdraw")
    print("c - Deposit")
    print("q - quit")
    return options[input("option? ")]

def check_balance_menu():
    global accountnumber
    balance = get_transactions(accountnumber)
    print(f"\nThe account number {accountnumber} has a balance of {balance}")
    input("go back? ")
    return 'standard_menu'

def withdraw_menu():
    withdraw = float(input ("\nHow much do you want to withdraw? "))
    newbalance = create_transaction(accountnumber, -withdraw,"withdraw")
    if(newbalance == None):
        print("The transaction was NOT successful\n")
        input("go back? ") 
        return'standard_menu'

    print(f"The transaction was successful. Your new balance is {newbalance}\n")
    input("go back? ")  
    return 'standard_menu'

def deposit_menu():
    deposit = float(input ("\nHow much do you want to deposit? "))
    newbalance = create_transaction(accountnumber, deposit, "deposit")
    print(f"The transaction was successful. Your new balance is {newbalance}")
    input("go back? ")  
    return 'standard_menu'
    

def admin_menu():
    print("select your option")
    print("a - create new acccount")
    print("b - Edit account")
    print("c - Close account")
    input("option?")    

if __name__ == "__main__":
    state = "login_menu"

    while True:

        if(state == 'login_menu'):
            state = login_menu()
        elif(state == 'standard_menu'):
            state = standard_menu()
        elif(state == 'check_balance_menu'):
            state = check_balance_menu()
        elif(state == 'withdraw_menu'):
            state = withdraw_menu()      
        elif(state == 'deposit_menu'):
            state = deposit_menu()
        elif(state == 'quit'):
            break
        pass
    print("\nhave a nice day")
