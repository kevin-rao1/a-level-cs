isbn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for count in range(1,14):
    isbn[count] = int(input("Please enter next digit of ISBN: "))
print(isbn)
CalculatedDigit = 0
count = 1
while count < 13:
    CalculatedDigit += isbn[count]
    count += 1
    CalculatedDigit += isbn[count]*3
    count += 1
    print(CalculatedDigit)
while CalculatedDigit >= 10:
    CalculatedDigit -= 10
    print(CalculatedDigit)
CalculatedDigit -= 10
if CalculatedDigit == 10:
    CalculatedDigit = 0
if CalculatedDigit == isbn[12]:
    print("Valid ISBN")
else:
    print("Invalid ISBN")