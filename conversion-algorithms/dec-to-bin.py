def convert_decimal_to_binary(decimal:int):
    binary = []
    if decimal == 0:
        return 0
    while not decimal == 0:
        dec_new = decimal//2
        binary.insert(0,decimal%2)
        decimal = dec_new
    return binary

if __name__ == "__main__":
    print(convert_decimal_to_binary(9008))