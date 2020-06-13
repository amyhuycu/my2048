from terminaltables import SingleTable
import random

table_data = [
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
    ['    ', '    ', '    ', '    '],
]

def draw_grid():
    table_data = [
        ['00', '01', '02', '03'],
        ['10', '11', '12', '13'],
        ['20', '21', '22', '23'],
        ['30', '31', '32', '33'],
    ]
    table_instance = SingleTable(table_data, 'Play Game')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center'}
    print(table_instance.table)

def draw_grid_init():
    
    table_data = [
        ['    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    '],
        ['    ', '    ', '    ', '    '],
    ]
    
    add_random()
    add_random()

    table_instance = SingleTable(table_data, 'Play Game')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center'}
    print(table_instance.table)

def draw_updated_grid():
    table_instance = SingleTable(table_data, 'Play Game')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center'}
    print(table_instance.table)

def move_up():
    print("UP")

def move_down():
    print("DOWN")

def move_left():
    print("LEFT")

def move_right():
    print("RIGHT")    

def add_random():
    print("RANDOM")
    # Choose random value (2 or 4)
    val = 0
    random_num = random.randint(0, 2)
    if random_num == 0:
        val = 2
    else:
        val = 4

    # Choose random column
    random_col = random.randint(0, 3)
    # Choose random row
    random_row = random.randint(0, 3)

    # Pick a new position if this one is invalid
    while (table_data[random_row][random_col] != '    '):
        # Choose random column
        random_col = random.randint(0, 3)
        # Choose random row
        random_row = random.randint(0, 3)
    
    table_data[random_row][random_col] = val


def main():
    draw_grid()
 
    user_input = input("Start Game: (Press any key and hit Enter)")
    if user_input:
        draw_grid_init()

    user_input = 'W'
    while user_input != 'Q':
        user_input = input("Choose a move: (Up = W, Left = A, Down = S, Right = D, Quit = Q) ")
        if (user_input == 'W' or user_input == 'w'):
            move_up()
        elif (user_input == 'A' or user_input == 'a'):
            move_left()
        elif (user_input == 'S' or user_input == 's'):
            move_down()
        elif (user_input == 'D' or user_input == 'd'):
            move_right()
        elif (user_input == 'Q' or user_input == 'q'):
            print("Quitting Game")
            exit()
        else:
            print("Invalid input! Try again")
            continue

        draw_updated_grid()
        add_random()
        draw_updated_grid()
        

if __name__ == "__main__":
    main()