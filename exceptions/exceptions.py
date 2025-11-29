usernames = ["You shouldn't see this",'Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']
# shifted by 1 to avoid zero division

class BadGuyError(Exception):
    pass

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
            if number == 6:
                raise BadGuyError
            division = 301 / number # if we don't change the user number system, we have to divide by 0 or never be able to log in as Cheetara.
            print("Welcome", usernames[number], "user number", number,".")
            break
        except (ValueError, IndexError, ZeroDivisionError) as WrongNumberError:
            usernumber = input("Enter valid usernumber: ")
    print(f"301 divided by {number} = {division}")

def login_handled_if(usernumber):
    print("\n -- Using if statements --\n")
    isCorrect = True
    if not usernumber.isdecimal(): # if isdecimal, then can always parse as int, unlike isnumeric or isdigit
        isCorrect = False
    elif int(usernumber) <= 0 or int(usernumber) > len(usernames): # prevent int(usernumber) from crashing when usernumber is not number
        isCorrect = False
    while not isCorrect:
        usernumber = input("Enter valid usernumber:")
        isCorrect = True
        if not usernumber.isdecimal():
            isCorrect = False
        elif int(usernumber) <= 0 or int(usernumber) > len(usernames):
            isCorrect = False
            # would be better to create a new function isCorrect and call while isCorrect(usernumber) == False

    number = int(usernumber)
    if number == 6:
        raise BadGuyError
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    try:
        login_handled_catchexcept(inp)
        login_handled_if(inp)
    except BadGuyError:
        print("a"*9008+" im screaming in lowercase")