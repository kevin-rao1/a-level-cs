bees = "bee20script.txt"


def read_and_display_files(filename):
    """reads the bees file and prints it"""
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")

def assemble_file_from_input(filename):
    """asks for input line by line to assemble and save a file"""
    with open(filename, "w") as file:
        file.write("") # clear the file
    with open(filename, "a") as file:
        line = 0
        while not isFinished:
            line_input = input(f"Text for line {line}: ")
            file.write(line_input)
            finished_prompt_answer = input("Are you finished? [y/N]")
            if finished_prompt_answer =="y": # any input not y is assumed to be no, as per convention
                isFinished = True
            else:
                isFinished = False
            line = line + 1

def menu():
    while True:
        print("""Select an option:
        1. Read a file
        2. Write a file (WILL OVERWRITE FILE!)""")
        while True:
            try:
                option = int(input(">"))
                break
            except ValueError:
                
        while int(option) not in (1, 2):
            option = input("Please choose option 1 or 2. \n>")

menu()