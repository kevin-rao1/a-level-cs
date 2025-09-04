"""
Notes: 
- Expanding to 3-digit number support is fairly trivial, but requires changing hardcoded values.
- Expanding to n-digit support may be more difficult, and of limited practicality.
- There's no automated checking for terminal support, as it's too platform-dependent.
- No AI was h̶a̶r̶m̶e̶d̶ used in the making of this program.
"""

while True:
    try:
        ##### Input handling
        print("Please note that this program is designed to be run on a monospaced terminal with ligature support and width greater than 35")
        lowest_number = int(input("Lowest integer in table axis: "))
        highest_number = int(input("Highest integer in table axis: "))

        while lowest_number >= highest_number + 1:
            print("Lowest value must be lower than highest. Please try again.")
            lowest_number = int(input("Lowest integer in table axis: "))
            highest_number = int(input("Highest integer in table axis: "))


        while lowest_number >= 10:
            print("Due to formatting issues, numbers greater than 9 are currently unsupported.")
            lowest_number = int(input("Lowest integer in table axis: ")) # ensure result is always 2 digits

        while highest_number >= 10:
            print("Due to formatting issues, numbers greater than 9 are currently unsupported.")
            highest_number = int(input("Highest integer in table axis: ")) # ensure result is always 2 digits again
        


        ##### Result Computation and Printing
        print("\nResults Table:")

        # core table
        for row in range(lowest_number, highest_number + 1):
            row_buffer = f"0{row} │"
            for column in range(lowest_number, row + 1): # current row number = number of things to calculate for row
                if row*column <= 9: # monospaced table formatting for always 2-digit numbers
                    row_buffer = row_buffer + f" 0{row*column}"
                else:
                    row_buffer = row_buffer + f" {row*column}"
                column = column + 1
            print(row_buffer)
            row = row + 1
        
        # footer
        table_horizontal_line = "───┼─" + (highest_number - lowest_number + 1)*"───"
        print(table_horizontal_line)
        x_axis_label = "   │"
        for i in range(lowest_number, highest_number + 1):
            x_axis_label = x_axis_label + f" 0{i}"
            i = i + 1
        print(x_axis_label)
        break
    except ValueError:
        print("Invalid input: Numbers must be integers. Please try again.")

"""
Example Output Structure: 

"
Results Table:

01 │ 01
02 │ 02 04
03 │ 03 06 09
04 │ 04 08 12 16
05 │ 05 10 15 20 25
───┼───────────────
   │ 01 02 03 04 05"
"""