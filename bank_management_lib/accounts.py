from .connect_db import cursor,Error,connection

first_random_number = 120231240

def find_user_with_aadhar_phone(aadhar_number,phone_number):
    cursor.execute(f"select * from users where aadhar_number={aadhar_number} and phone_number={phone_number}")
    for (fn,dob,pn,ba,an,acn) in cursor:
        return True
    return False

def create_user(fn,dob,pn,ba,an,acn):
    return { "fullname": fn,
            "dob": dob,
            "phone_number": pn,
            "balance": ba,
            "aadhar_number": an,
            "account_number": acn
        }

def find_user_with_account_number(account_number):
    
    cursor.execute(f"select * from users where account_number={account_number}")
    for (fn,dob,pn,ba,an,acn) in cursor:
        return create_user(fn,dob,pn,ba,an,acn)
    return False

def check_user(user):
    if not user:
        print("\tno user found with that account number..")
        return False
    return True

def create_new_account():
    global first_random_number
    fullname = input("enter your full name = ")
    dob = input("enter you dob[dd-mm-yyyy] = ")
    phone_number = input("enter phone number = ")
    opening_balance = int(input("enter balance = "))
    aadhar_number = input("enter aadhar number = ")
    if(find_user_with_aadhar_phone(aadhar_number,phone_number)):
        print("\tuser already exists with that aadhar or phone number..")
        return
    first_random_number += 1
    query = ("INSERT INTO users "
            "(fullname, dob, phone_number, balance, aadhar_number, account_number) "
            "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (fullname,dob,phone_number,opening_balance,aadhar_number,first_random_number)
    try:
        cursor.execute(query,data)
        connection.commit()
    except Error as e:
        print("new user error",e.msg)

    print(f"\tyour account number : {first_random_number}")

def close_account(account_number):
    user = find_user_with_account_number(account_number)
    if(check_user(user)):
        cursor.execute("delete from users where account_number=%s",(account_number,))
        connection.commit()
    else:
        print("\tno user found with that account number")



def display_account_details(account_number):
    user = find_user_with_account_number(account_number)
    if(check_user(user)):
        print(f"\taccount_number : {account_number}")
        print("\tusername :",user["fullname"])
        print("\tbalance :",user["balance"])
        print("\tphone_number :",user["phone_number"])
        print("\taadhar_number :",user["aadhar_number"])

def check_balance(account_number):
    user = find_user_with_account_number(account_number)
    if(check_user(user)):
        print(f"\taccount_number : {account_number}")
        print("\tusername :",user["fullname"])
        print("\tbalance :",user["balance"])

def withdraw_amount(account_number,amount):
    user = find_user_with_account_number(account_number)
    if(check_user(user)):
        if user["balance"] >= amount:
            user["balance"] -= amount
            cursor.execute("update users set balance=%s where account_number=%s",(user["balance"],account_number))
            connection.commit()
            print(f"\twithdraw succesfull of amount {amount}")
            print("\tcurrent balance is :",user["balance"])
        else:
            print("\t amount exceeded for withdrawl")

def deposit_amount(account_number,amount):
    user = find_user_with_account_number(account_number)
    if(check_user(user)):
        user["balance"] += amount
        cursor.execute("update users set balance=%s where account_number=%s",(user["balance"],account_number))
        connection.commit()
        print("\tcurrent balance is :",user["balance"])

def transfer_amount(src_account_number,dst_account_number,amount):
    src_user = find_user_with_account_number(src_account_number)
    dst_user = find_user_with_account_number(dst_account_number)
    if check_user(src_user) and check_user(dst_user):
        src_user["balance"] -= amount
        cursor.execute("update users set balance=%s where account_number=%s",(src_user["balance"],src_account_number))
        dst_user["balance"] += amount
        cursor.execute("update users set balance=%s where account_number=%s",(dst_user["balance"],dst_account_number))
        connection.commit()
