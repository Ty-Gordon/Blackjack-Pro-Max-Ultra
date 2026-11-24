
users = []

def read():
    with  open ("logins.txt", "r") as logins:
        for x in logins:
            bartSimpson = x.split("`")
            users.append(bartSimpson)
    

def write():
    temp = []
    with open ("logins.txt", "w") as logins:
        for x in range(len(users)):
            temp.append("`".join(users[x]))
            logins.write(temp[x])

def newUser():
    ex = 0
    loopCondition = 0
    
    print("enter 'r' to return home\n\n")
    while loopCondition == 0:
        loopCondition = 1
        user = input("enter your username: ")
        
        for x in range(len(users)):
            if user == users[x][0]:
                loopCondition = 0
                print("username already taken")
        
        if "`" in user:
            print("username cannot contain '`' character")
            loopCondition = 0
        
        if user.lower() == "r":
            print("")
            ex = 1
            loopCondition = 1
    
    if ex != 0:
        loopCondition = 1
    else:
        loopCondition = 0
            
    while loopCondition == 0:
        password  = input("enter your password: ")
        
        if "`" not in password:
            loopCondition = 1
        else:
            print("password must not contain '`' character")
        
        if password == "r":
            print("")
            ex = 1
        
    
    if ex != 1:
        users.append([user, password, "10000" + "\n"])
        return ex
    else:
        return ex

def validation():
    position = 0
    ex = 0
    the = 0
    loopCondition = 0
    
    print("enter 'r' to return home\n\n")    
    while loopCondition == 0:    
        user = input("enter your username")
        for x in range(len(users)):
            if users[x][0] == user:
                position = x
                the = 1
        
        if the > 0:
            loopCondition = 1
        elif user.lower() == "r":
            print("")
            loopCondition = 1
            ex = 1
            
        else:
            print("user not found")
    
    loopCondition = 0
    if ex > 0:
        loopCondition = 1
        
    attempts = 0
    success = 0
    if ex < 1:
        password = users[position][1]
    
    while loopCondition == 0 and attempts < 3:
        pw = input("enter your password")
        if pw.lower() == "r":
            print("")
            loopCondition = 1
            ex = 1
        elif pw == password:
            loopCondition = 1
            success = 1
        else:
            attempts += 1
            print("incorrect password")
            print(f"remaining attempts: {3 - attempts}")
            
    if ex < 1:
        if  success < 1:
            print("login failed")
            
        elif success > 0:
            print("login successful")
        
    return success, position, ex
    
def begin():
    read()
    loopCondition = 0
    success = 0

    while loopCondition == 0:
        choice = input("Choose:\n(1) - New User\n(2) - Existing User\n")
        print("\n")
        if choice == "1":
            the = newUser()
            loopCondition = 1
            if the < 1:
                success = 1
                position = len(users) -  1
            else:
                loopCondition = 0
        elif choice == "2":
            loopCondition = 1            
            the = validation()
            if the[2] < 1:
                success = the[0]
                position = the[1]
            else:
                loopCondition = 0
        else:
            print("invalid input")
    
    return success, position

        
