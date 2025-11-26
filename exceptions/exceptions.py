usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


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
            print("Welcome", usernames[number], "user number", number,".")
            division = 301 / number
            break
        except (ValueError, IndexError, ZeroDivisionError) as wrongnumber:
            usernumber = input("Enter valid usernumber: ")
    print(f"301 divided by {number} = {division}")

def login_handled_if(usernumber):
    print("\n -- Using if statements --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_handled_catchexcept(inp)

