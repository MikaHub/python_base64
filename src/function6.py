list = ["010000","010100","001001","000011","010001","000000"]

def convert6bits(list):
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of bits to integer
    # Then returns the new list
    bitsconverted = []
    for bits in list:
        bitsconverted.append(int(bits, 2))
    return bitsconverted


print(convert6bits(list))