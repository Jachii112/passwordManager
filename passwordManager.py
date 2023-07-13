masterPwd = input("What is the master password?")

def view():
      with open('password.txt', 'r') as f: 
        for line in f.readlines():
            data = line.rsplit()
            user, passw = data.split("|")
            print("User: ", user, " | Password: ", passw)

def add():
    name = input('Account Name: ')
    pwd = input('Account Password: ')
    
    with open('password.txt', 'a') as f: 
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add new password or view existing password (view, add), press q to quit?").lower()

    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue