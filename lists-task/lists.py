name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
print(f"The third name is: {name_list[1]}")
print("The last 7 names are: ")
for i in range(len(name_list)-8, len(name_list)):
    print(f"{name_list[i]} ")

number_list = []
for i in range(5):
    number_list.append(int(input("Type in a number: ")))
print(f"largest: {max(number_list)}")
print(f"smallest: {min(number_list)}")
print(f"mean: {sum(number_list)/5}")