from logger import input_data, read_data, change_data, delete_data


def interface():
    print(f'Hello! Choose command: \n 1: write data \n 2: read data \n'
          f'3: change data \n 4: delete data \n')
    command = int(input('Enter command: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print('Wrong command')
        command = int(input('Enter command: '))

    if command == 1:
        input_data()
    elif command == 2:
        read_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()


interface()