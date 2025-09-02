while True:
    try:
        base_number = int(input("Base number to multiply: "))
        for i in range(1,12):
            print(base_number*i)
            i = i + 1
        break
    except ValueError:
        print("Invalid input: Number must be integer")
