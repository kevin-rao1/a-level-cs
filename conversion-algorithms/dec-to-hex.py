def convert_decimal_to_base(decimal:int, base:int):
    binary = ""
    if decimal == 0:
        return 0
    while not decimal == 0:
        binary = str(decimal%base) + binary
        decimal = decimal//base
    return "0x"+binary if base==16 else "0b" if base ==2 else ""

if __name__ == "__main__":
    print(convert_decimal_to_base(36872, 16))