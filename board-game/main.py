"""This file contains the game main loop, while the other file handles rendering and logic.
Development:
Wrote everything apart from draw_board(), 
then used Gemini 3 to implement draw_board() to test the rest of the logic, 
then wrote my own draw_board() once the rest of the code was working. 
A commit with the AI draw_board() is available.

Issues:
- Screen flickers due to improper use of os.system
- Keyboard library requires elevated permissions on UNIX
- Input debouncing is badly handled due to improper use of Keyboard."""

# setup
from sys import platform
import os
import time
cls = "clear" # clearing screen uses system command.
if platform == "win32": # all windows apart from cygwin or msys32 reports as win32.
    cls = "cls"
try:
    import keyboard
except ImportError:
    print("Please install the keyboard library. ")
    exit()
print("Libraries loaded.")
width = 3
height = 3
current_player = "X" # options are X, O
winner = "Nobody" # options are Nobody, Tie, X, O
move = 1
number_to_win = 3
board = [" " for i in range(width*height)] # " " for empty, "O" for nought, "X" for cross
selected_location = ((width*height)//2)-(width//2) # defaults close to middle of board

# function definitions
def draw_board():
    # 1. Clear the screen (Cross-platform safe)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Turn for {current_player}\nMove {move}")

    # AI Generated code starts here based on a broken implementation I did earlier.
    # 2. Calculate the X (col) and Y (row) of the selection
    sel_col = selected_location % width
    sel_row = selected_location // width

    # 3. Iterate through every grid row
    for r in range(height):
        # --- DRAW THE TOP LINE OF THE ROW ---
        line_str = ""
        for c in range(width):
            # Determine intersection char (simplified to + for logic clarity, 
            # or you can use ┌┬┐ logic if you want strict corners)
            if r == 0:
                corner = "┌" if c == 0 else "┬"
            else:
                corner = "├" if c == 0 else "┼"
            
            # Check if this specific cell is the top of the selected box
            # or the bottom of the selected box from the previous row
            if (r == sel_row and c == sel_col):
                # Top of selection (uses thick line)
                line_str += corner + "═══" 
            elif (r == sel_row + 1 and c == sel_col): 
                # Bottom of selection (conceptually top of this row, thick line)
                 line_str += corner + "═══"
            else:
                # Normal line
                line_str += corner + "───"
        
        # Close the line (Rightmost edge)
        if r == 0:
            line_str += "┐"
        else:
            line_str += "┤"
        print(line_str)

        # --- DRAW THE CONTENT OF THE ROW ---
        content_str = ""
        for c in range(width):
            cell_char = board[r*width+c] 

            # Determine left border style
            # If this cell is selected, OR the one to the left was selected
            if (r == sel_row and c == sel_col):
                border = "║"
            elif (r == sel_row and c == sel_col + 1):
                border = "║"
            else:
                border = "│"
            
            content_str += f"{border} {cell_char} "
        
        # Close the content row (Rightmost edge)
        # If the last cell in this row was selected, needs thick closing border
        if r == sel_row and (width - 1) == sel_col:
            content_str += "║"
        else:
            content_str += "│"
            
        print(content_str)

    # 4. DRAW THE VERY BOTTOM LINE
    bottom_str = ""
    for c in range(width):
        corner = "└" if c == 0 else "┴"
        
        # Check if this is the bottom of the selected cell
        if (height - 1 == sel_row and c == sel_col):
            bottom_str += corner + "═══"
        else:
            bottom_str += corner + "───"
    bottom_str += "┘"
    print(bottom_str)
    # AI Generated code ends here

def coord_transform(x:int, y:int):
    """maps a coordinate, (x,y) to a single index number"""
    return y*width+x

def check_for_win_state():
    global winner # scope issue, had to use AI to debug this one. 
    if move == (width*height)+1: # board full
        winner = "Tie" 
    
    for row in range(height): # check horizontal
        Xcount = 0
        Ocount = 0
        for item in range(width):
            cell = board[(row*width)+item]
            if cell == "X": # how do I simplify this?
                Xcount += 1
                Ocount = 0
            if cell == "O":
                Ocount += 1
                Xcount = 0
            if cell == " ":
                Xcount = 0
                Ocount = 0
            if Xcount >= number_to_win:
                winner = "X"
                return 
            if Ocount >= number_to_win:
                winner = "O"
                return
    
    for column in range(width): # check vertical
        Ocount = 0
        Xcount = 0
        for row in range(height):
            cell = board[row*width+column]
            if cell == "X":
                Xcount += 1
                Ocount = 0
            if cell == "O":
                Ocount += 1
                Xcount = 0
            if cell == " ":
                Xcount = 0
                Ocount = 0
            if Xcount >= number_to_win:
                winner = "X"
                return 
            if Ocount >= number_to_win:
                winner = "O"
                return
        
draw_board()

# Main loop
while winner == "Nobody":
    event = keyboard.read_event(suppress=True)
    if event.event_type == keyboard.KEY_DOWN:
        moved = False
        
        if event.name == "left":
            selected_location = (selected_location//width)*width + (selected_location%width - 1)%width 
            moved = True
        elif event.name == "right":
            selected_location = (selected_location//width)*width + (selected_location%width + 1)%width 
            moved = True
        elif event.name == "up":
            selected_location = (selected_location - width)%(height*width)
            moved = True
        elif event.name == "down":
            selected_location = (selected_location + width)%(height*width)
            moved = True
        elif event.name == "enter":
            if board[selected_location] == " ":
                board[selected_location] = current_player
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
                move += 1
                moved = True
                check_for_win_state()
        elif event.name == "esc": # Good practice to add an emergency exit
            print("Game exited.")
            exit()

        if moved:
            draw_board()


# win display
os.system(cls)
if winner == "Tie":
    print(f"""┌───────────┐
│It's a tie.│
└───────────┘""")
else:
    print(f"{winner} has won the game.")
exit()