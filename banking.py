import mysql.connector
from datetime import date

def clear():
    for i in range(50):
        print()

def acc_status(AccountID):
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    sql = "select Status, Balance from Accounts where AccountID =' " +AccountID+ " ' "
    result = cursor.execute(sql)
    result = cursor.fetchone()  
    conn.close()
    return result

def deposit(AccountID, amount):
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    AccountID = input("Enter Account ID: ")
    amount = input("Enter Amount to Deposit: ")
    today = date.today()
    result = acc_status(AccountID)
    if result == 'Active':
        sql1 = "update Accounts set Balance = Balance + " + amount + " where AccountID = " + AccountID + " and Status = 'Active';"
        sql2 = "insert into Transactions (AccountID, TransactionDate, Amount, TransactionType) values (" + AccountID + ", '" + str(today) + "', " + amount + ", 'Deposit');"
        cursor.execute(sql1)
        cursor.execute(sql2)
        print("\n\nAmount Deposited Successfully")
    
    else:
        print('\n\nAccount is not Active')
        
        wait= input("\n\nPress any key to continue")
        conn.close()

def withdraw(AccountID, amount):
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    AccountID = input("Enter Account ID: ")
    amount = input("Enter Amount to Withdraw: ")
    today = date.today()
    result = acc_status(AccountID)

    if result == 'Active':
        if result[1] >= amount:
            sql1 = "update Accounts set Balance = Balance - " + amount + " where AccountID = " + AccountID + " and Status = 'Active';"
            sql2 = "insert into Transactions (AccountID, TransactionDate, Amount, TransactionType) values (" + AccountID + ", '" + str(today) + "', " + amount + ", 'Withdraw');"
            cursor.execute(sql1)
            cursor.execute(sql2)
            print("\n\nAmount Withdrawn Successfully")
        else:
            print("\n\nInsufficient Balance OR Account is not Active")
            wait = input("\n\nPress any key to continue")
            conn.close()

def transaction_menu():
    clear()
    print("\n1. Deposit")
    print("\n2. Withdraw")
    print("\n3. Main menu")
    choice = input("Enter Choice: ")
    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        main_menu()
        
    else:
        print("Invalid Choice")
        wait = input("\n\nPress any key to continue")
        transaction_menu()

def search_menu():
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    print("\n1. Search by Account ID")
    print("\n2. Search by Adhar Number")
    print("\n3. Main menu")
    choice = input("Enter Choice: ")
    field_name= ''
    if choice == '1':
        field_name = 'AccountID'
    elif choice == '2':
        field_name = 'AdharNumber'
    elif choice == '3':
        main_menu()

    msg = "Enter " + field_name + ": "
    value= input(msg)
    if field_name == 'AccountID':
        sql1 = "select * from Accounts where AccountID = " + value + ";"
    else:
        sql1 = "select * from Customers where adharno = '" + value + "');"

    cursor.execute(sql1)
    records= cursor.fetchall()
    
    if not records:
        print("No records found")
    else:
        for record in records:
            print(record)
    
    wait = input("\n\nPress any key to continue")
    search_menu()
    conn.close()




def add_account():
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    print("Add Account")
    CustomerName= input("Enter Customer Name: ")
    AdharNumber = input("Enter Adhar Number: ")
    Email = input("Enter Email: ")
    MobileNumber = input("Enter Mobile Number: ")
    AccountType = input("Enter Account Type: ")
    Balance = input("Enter Balance: ")
    Status = input("Enter Status: ")
    sql1= "insert into Customers ('name', 'adharno', 'phoneNumber', 'email') values ('" + CustomerName + "', '" + AdharNumber + "', '" + MobileNumber + "', '" + Email + "');"
    sql2 = "insert into Accounts ('AccountType', 'Balance', 'Status') values ('" + AccountType + "', " + Balance + ", '" + Status + "');"
    cursor.execute(sql1)
    cursor.execute(sql2)
    conn.commit()
    print("\n\nAccount Added Successfully")
    wait = input("\n\nPress any key to continue")
    conn.close()

def modify_account():
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    accountID = input("Enter Account ID: ")
    print("Modify Account")
    print("\n1. Name")
    print("\n2. Adhar Number")
    print("\n3. Email")
    print("\n4. Mobile Number")
    choice= int (input("Enter Choice: "))
    new_data = input("Enter New Value: ")
    field_name = ''
    if choice == 1:
        field_name = 'name'
    elif choice == 2:
        field_name = 'adharno'
    elif choice == 3:
        field_name = 'email'
    elif choice == 4:
        field_name = 'phoneNumber'
    else:
        print("Invalid Choice")
        wait = input("\n\nPress any key to continue")
        modify_account()

    sql1 = "update Customers set " + field_name + " = '" + new_data + "' where AccountID = " + accountID + ";"
    cursor.execute(sql1)
    conn.commit()
    print("\n\nAccount Modified Successfully")
    wait = input("\n\nPress any key to continue")
    conn.close()

def close_account():
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    accountID = input("Enter Account ID: ")
    sql1 = "update Accounts set Status = 'Closed' where AccountID = " + accountID + ";"
    cursor.execute(sql1)
    conn.commit()
    print("\n\nAccount Closed Successfully")
    wait = input("\n\nPress any key to continue")
    conn.close()

def activate_account():
    conn = mysql.connector.connect(host='localhost', user='root', password='P@ssw0rd', database='bankProject')
    cursor = conn.cursor()
    clear()
    accountID = input("Enter Account ID: ")
    sql1 = "update Accounts set Status = 'Active' where AccountID = " + accountID + ";"
    cursor.execute(sql1)
    conn.commit()
    print("\n\nAccount Activated Successfully")
    wait = input("\n\nPress any key to continue")
    conn.close()

def main_menu():
    clear()
    print("Main menu")
    print("\n1. Add Account")
    print("\n2. Modify Account")
    print("\n3. Close Account")
    print("\n4. Activate Account")
    print("\n5. Transaction menu")
    print("\n6. Search Menu")
    print("\n7. Exit")
    choice = input("Enter Choice: ")
    if choice == '1':
        add_account()
    elif choice == '2':
        modify_account()
    elif choice == '3':
        close_account()
    elif choice == '4':
        activate_account()  
    elif choice == '5':
        transaction_menu()
    elif choice == '6':
        search_menu()
    elif choice == '7':
        exit()    
    else:
        print("Invalid Choice")
        wait = input("\n\nPress any key to continue")
        main_menu()
if __name__ == "__main__":
    main_menu()


        


