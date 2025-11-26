usernames = ["You shouldn't see this",'Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']
# shifted by 1 to avoid zero division

def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")

def login_handled_catchexcept(usernumber):
    print("\n -- Using try/except --\n")
    while True: # scary
        try:
            number = int(usernumber)
            division = 301 / number # if we don't change the user number system, we have to divide by 0 or never be able to log in as Cheetara.
            print("Welcome", usernames[number], "user number", number,".")
            break
        except (ValueError, IndexError, ZeroDivisionError) as wrongnumber:
            usernumber = input("Enter valid usernumber: ")
    print(f"301 divided by {number} = {division}")

def login_handled_if(usernumber):
    print("\n -- Using if statements --\n")
    if not usernumber.isdecimal():
        correct = False
    elif int(usernumber) <= 0 or int(usernumber) > len(usernames):
        correct = False
    while not correct:
        usernumber = input("Enter valid usernumber:")
        correct = True
        if not usernumber.isdecimal():
            correct = False
        elif int(usernumber) <= 0 or int(usernumber) > len(usernames):
            correct = False
            # would be better to create a new function isCorrect and call while isCorrect(usernumber) == False
    
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_handled_catchexcept(inp)
    login_handled_if(inp)

