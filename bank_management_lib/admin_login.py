admins_users = [{"shakeel":123},{"lalu":456}]

    
login = False

def isAuthenticated():
    global login
    return login

def authenticate():
    global login
    login_username = input("enter username = ")
    login_password = input("enter password = ")

    for user in admins_users:
        if user.get(login_username) and user.get(login_username) == int(login_password):
            login = True

authenticate()