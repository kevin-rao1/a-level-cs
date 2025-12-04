input_str = ""
with open("advent-of-code-2025/input", "r") as input_txt:
    for line in input_txt:
        input_str += line
input_list = input_str.split("\n")
position = 50
NoOfZeroes = 0
for move in input_list:
    direction = move[0]
    if direction == "L":
        for i in range(int(move[1:])):
            position = (position-1)%100
            if position == 0:
                NoOfZeroes += 1
    if direction == "R":
        for i in range(int(move[1:])):
            position = (position+1)%100
            if position == 0:
                NoOfZeroes += 1
    
print(NoOfZeroes) # 1081