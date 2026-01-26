# code for Q1a
letter_coords = [i for i in input("Letters in uppercase: ")]
assert "Z" not in letter_coords
noof_letters = len(letter_coords) #5^n

# convert letter coords to number coords, zero-indexed, 0=top
# e.g.: R -> [2,3]
y = [["A", "B", "C", "D", "E"],["F", "G", "H", "I", "J"],["K", "L", "M", "N", "O"],["P", "Q", "R", "S", "T"],["U", "V", "W", "X", "Y"]]
x = [["A", "F", "K", "P", "U"],["B", "G", "L", "Q", "V"],["C", "H", "M", "R", "W"],["D", "I", "N", "S", "X"],["E", "J", "O", "T", "Y"]]

number_coords = []

for i in letter_coords:
    i_coord = []
    for j in range(len(x)):
        if i in x[j]:
            i_coord.append(j)
            break
    for k in range((len(y))):
        if i in y[k]:
            i_coord.append(k)
            break
    number_coords.append(i_coord)

# merge coords into one large coord
# [[2, 1], [4, 2], [5, 3]] (BIO) becomes [45, 118]

final_x = 0
final_y = 0

for i in range(len(number_coords)):
    # read least significant coord first
    item = len(number_coords)-1-i
    #print(number_coords[item])
    # get the x and y values in zero-indexed form
    x_val=number_coords[item][0]
    y_val=number_coords[item][1]
    
    significance = 5**i #multiplier to get the order. 1, then 5ths, then 15ths, kind of like base-5

    final_x += x_val*significance
    final_y += y_val*significance

    #print(significance, "|", x_val*significance, y_val*significance, "|", final_x, final_y)

final_x += 1
final_y = 5**noof_letters - final_y # convert back to 1=bottom
print(final_x,final_y)
