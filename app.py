from bank_management_lib.admin_login import authenticate, isAuthenticated
from bank_management_lib.accounts import check_balance, close_account, create_new_account, deposit_amount, display_account_details, transfer_amount, withdraw_amount
from bank_management_lib.connect_db import connection,cursor

def main():

    while True:
        if(isAuthenticated()):
            print("1. create new account")
            print("2. deposit amount")
            print("3. withdraw amount")
            print("4. balance enquiry")
            print("5. display account details")
            print("6. transfer amount")
            print("7. close an account")
            print("8. exit")

            user_choice = int(input("enter your choice = "))
            if user_choice == 1:
                create_new_account()
            elif user_choice == 2:
                account_number = int(input("enter account number = "))
                amount = int(input("enter amount to deposit = "))
                deposit_amount(account_number,amount)
            elif user_choice == 3:
                account_number = int(input("enter account number = "))
                amount = int(input("enter amount to withdraw = "))
                withdraw_amount(account_number,amount)
            elif user_choice == 4:
                account_number = int(input("enter account number = "))
                check_balance(account_number)
            elif user_choice == 5:
                account_number = int(input("enter account number = "))
                display_account_details(account_number)
            elif user_choice == 6:
                amount = int(input("enter amount to transfer = "))
                src_account_number = int(input("enter source account number = "))
                dst_account_number = int(input("enter destination account number = "))
                transfer_amount(src_account_number=src_account_number,dst_account_number=dst_account_number,amount=amount)
            elif user_choice == 7:
                account_number = int(input("enter account number = "))
                close_account(account_number)
            elif user_choice == 8:
                cursor.close()
                connection.close()
                exit()

        else:
            print("you are not authenticated...")
            print("please authenticate..")
            authenticate()

if(__name__ == "__main__"):
    main()