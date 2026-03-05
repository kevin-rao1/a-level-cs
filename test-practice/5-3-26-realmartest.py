"""
OUTPUT "Enter integer (0-99):"
INPUT Value
OUTPUT "Calculate additive or multiplicative persistence (a or m)?"
INPUT Operation
Count ← 0
WHITE Value > 9
IF Operation = "a" THEN
Value ← (Value DIV 10) + (Value MOD 10)
ELSE
Value ← (Value DIV 10) * (Value MOD 10)
ENDIF
Count ← Count + 1
ENDWHILE
OUTPUT "The persistence is: "
OUTPUT Count
"""
value = int(input("Enter integer (0-99): "))
operation = input("Calculate additive or multiplicative persistence (a or m)?")
count = 0
while value > 9:
    if operation == "a":
        value = (value//10) + (value%10)
    else: 
        value = (value//10) * (value%10)
    count += 1
print(f"The persistence is: {count}")
