noOfDigits = int(input("Enter number of digits: "))
input = [input(f"digit {i+1}: ") for i in range(noOfDigits)]
digits = [0 for i in range(10)]
for i in input:
    digits[int(i)] += 1
noOfMaxDigits = 0
for i in range(10):
    if digits[i] == max(digits):
        currentMax = i
        noOfMaxDigits +=1
if noOfMaxDigits>1:
    print("Data was multimodal")
else:
    print(f"{currentMax} was displayed {max(digits)} times.")