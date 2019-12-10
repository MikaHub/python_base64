def charListToInt(list):
    listOfInt = []
    for element in list:
        listOfInt.extend(ord(num) for num in element)
    return listOfInt    

 
list = ['A', 'B', 'C','D']
print(charListToInt(list))