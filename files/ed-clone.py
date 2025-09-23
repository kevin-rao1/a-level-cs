try:
    import argparse
except ImportError:
    print("Please install argparse.")
    exit(1)

print("""A badly written clone of the UNIX ed text editor.
      (see https://en.wikipedia.org/wiki/Ed_(software) and
      https://www.redhat.com/en/blog/introduction-ed-editor)
      Basic line editing commands are supported. Regex is not.
      ED is very user-unfriendly. Be careful with data loss!""")
parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", default=None, help="the file to edit")
args = parser.parse_args()

# set up initial state
linebuffer = []
dot = 0
filename = args.filename
modified = False

while True:
    main(linebuffer, dot, filename, modified)

def main(linebuffer, dot, filename, modified):
    modeselect()
    if filename:
        try:
            with open(filename, "r") as file:
                
def modeselect():
    mode = input(">")
    if mode == 'e':
        edit_mode()
    if mode == 'r':
        read_file()
    elif mode == 'w':
        write_file()
    elif mode == 'q':
        quit_editor()
    else:
        print("Invalid mode. Please select again.")
        modeselect()