def convert_denary_to_base(denary:float, base:int):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWZYZ"
    denary_int = int(denary)
    decimal = denary-denary_int # might have floating point errors?

    #process integer with repeated division
    output_int = ""
    if denary_int == 0:
        output_int = 0
    while not denary_int == 0:
        output_int = digits[denary_int%base] + output_int
        denary_int = denary_int//base

    # process decimal part with repeated multiplication
    output_dec = ""
    if decimal == 0:
        output_dec = 0
    while not decimal == 0:
        decimal *= base
        output_dec += digits[int(decimal)]
        decimal -= int(decimal)

    output = output_int+"."+output_dec
    return "0x"+output if base==16 else "0b"+output if base==2 else output

if __name__ == "__main__":
    print(convert_denary_to_base(1478.5626220703125, 16))
    print(convert_denary_to_base(3647.2564, 2))