from main import *

accountnumber = 0

def print_header():
    print('\n************************************************************')

def create_new_user_account():
    new_account_name = input('\nwhat is the name of the new account? ')
    new_account_lastname = input('what is the last name? ')
    new_account_address = input('what is the address? ')
    new_account_pin = input('what is the pin? ')
    accountnumber = createaccount(new_account_name, new_account_lastname, new_account_address, new_account_pin)
    print(f"Account created successfully. Your new account's number is: {accountnumber}")
    input("go back? ")
    return 'standard_menu'


def login_menu():
    global accountnumber
    next_state = ""
    print("\nWelcome to the bank system. Please enter your account number and pin.\n")
    accountnumber = int(input("Account number? "))
    db_pin = get_pin(accountnumber)

    if(db_pin == None):
        user_new_account = input("Account number does not exist. Would you like to make a new one? ")
        if user_new_account == "yes":
            return "create_new_user_account"
        else:
            return "login_menu"

    pin = int(input("PIN? "))
    usertype = get_user_type(accountnumber)

    if (pin == db_pin) and (usertype == "admin"):
        print('\nWelcome to the admin menu')
        next_state = 'admin_menu'
    elif (pin == db_pin) and (usertype == "customer"):
        print("\nYou have logged in successfuilly")
        next_state= 'standard_menu'
    else:
        input("PIN nummber is incorrect.")
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
    
def create_account():
    new_account_name = input('\nwhat is the name of the new account? ')
    new_account_lastname = input('what is the last name? ')
    new_account_address = input('what is the address? ')
    new_account_pin = input('what is the pin? ')
    newaccount = createaccount(new_account_name, new_account_lastname, new_account_address, new_account_pin)
    print(f"Account created successfully. Your new account's number is: {newaccount}")
    input("go back? ")
    return 'admin_menu'

def delete_account():
    delete = input("\nwhich account would you like to delete? ")
    deleteaccount(delete)
    print(f"account delete successfully.")
    input("go back? ")
    return 'admin_menu'

def edit_account():
    account_to_edit = input("\nWhat's the account number you want to edit? ")
    edit_options = {"a":"name", "b":"lastname", "c":"address", "d":"pin", "q":"quit"}
    print("a - First Name")
    print("b - Last Name")
    print("c - address")
    print("d - pin")
    print("q - quit")
    column = input("\nWhat do you want to change? ")
    if column == "q":
        return "admin_menu"
    new_val = input('what do you want to change it to? ')
    editaccount(account_to_edit, edit_options[column], new_val)
    print('Account was successfully changed')
    input("go back? ")
    
    return 'admin_menu'

def admin_menu():
    admin_options = {"a":"create_account", "b":"edit_account", "c":"delete_account", "q":"quit"}

    print("\nselect your options")
    print("a - Create new acccount")
    print("b - Edit account")
    print("c - Close account")
    print("q - quit")
    return admin_options[input("option? ")]

if __name__ == "__main__":
    state = "login_menu"

    while True:

        print_header()
        if(state == 'login_menu'):
            state = login_menu()
        if(state == 'create_new_user_account'):
            state = create_new_user_account()
        elif(state == 'standard_menu'):
            state = standard_menu()
        elif(state == 'admin_menu'):
            state = admin_menu()
        elif(state == 'create_account'):
            state = create_account()
        elif(state == 'delete_account'):
            state = delete_account()
        elif(state == 'edit_account'):
            state = edit_account()
        elif(state == 'check_balance_menu'):
            state = check_balance_menu()
        elif(state == 'withdraw_menu'):
            state = withdraw_menu()      
        elif(state == 'deposit_menu'):
            state = deposit_menu()
        elif(state == 'quit'):
            break
    print("\nhave a nice day\n")
