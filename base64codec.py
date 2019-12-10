from src import function1

def main():
    print('Base 64')
    while True:
        user_input = input('enter string or x to quit')

        if user_input.upper() == 'X':
            print('exit')
            break


        encoded_string = function1.convert_string_to_list(user_input)
        print(test)

if __name__ == "__main__":

    main()