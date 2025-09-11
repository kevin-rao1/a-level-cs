name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

for i in range(3):
    name = input(f"Type in name {i + 1} of 3: ")
    name_list.append(name)
print(name_list)
print(f"The third name is: {name_list[2]}")
print(f"The last 7 names are: {name_list[-7:]}")

number_list = []
while True:
    try:
        number_count = int(input("Number of numbers to add: "))
        for i in range(number_count):
            number_list.append(float(input(f"Type in number {i + 1} of {number_count}: ")))
        break
    except ValueError:
        print("Number of numbers to add must be integer")
print(f"largest: {max(number_list)}")
print(f"smallest: {min(number_list)}")
print(f"sum: {sum(number_list)}")
print(f"mean: {sum(number_list)/len(number_list)}")