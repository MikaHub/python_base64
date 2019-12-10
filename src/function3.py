list = [65, 66, 67, 68]

def convert8bits(list):
    # This function takes the list as parameter
    # Then create a list
    # Then converts the list of character to ascii
    
    # Then returns the new list
    converted8bits = []
    for ascii in list:
        
        converted8bits.append(format(ascii, '08b'))
    print(converted8bits)
    return converted8bits

print(convert8bits(list))


