Value = int(input("Enter integer (0-99): "))
Operation = input("Calculate additive or multiplicative persistence (a or m)? ")

Count = 0
while Value > 9:
    if Operation == "a":
        Value = (Value/10) + (Value%10)
    else:
        Value = (Value/10) * (Value%10)
    Count = Count + 1

print(f"The persistence is {Count}")