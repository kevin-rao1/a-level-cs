decimal = int(input("Enter decimal to convert: "))
binary = []
if decimal == 0:
    print(0)
    exit()
while not decimal == 0:
    binary.append(decimal%2)
    decimal = decimal//2
binary = reversed(binary) # what's a queue?
binary_str = ""
for i in binary:
    binary_str += str(i)
print(binary_str)