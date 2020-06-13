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
    up_ok = toggle('up')

    # Repeat for each column
    for column in range(4):
        # Get the row data
        row_data = []
        for row in range(4):
            if table_data[row][column] != '    ':
                row_data.append(table_data[row][column])

        # Combine within list of row data
        for item in range(len(row_data) - 1):
            if (item + 1) >= len(row_data):
                break
            if row_data[item] == row_data[item + 1]:
                row_data[item] = 2 * row_data[item + 1]
                row_data.pop(item + 1)
        
        # Put in placeholder spaces
        if (len(row_data) < 4):
            for amt in range(4 - len(row_data)):
                row_data.append('    ')

        # Update table_data
        for item in range(len(row_data)):
            table_data[item][column] = row_data[item]

def move_down():
    print("DOWN")
    down_ok = toggle('down')
    
    # Repeat for each column
    for column in range(4):
        # Get the row data
        row_data = []
        for row in range(3, -1, -1):
            if table_data[row][column] != '    ':
                row_data.append(table_data[row][column])

        # Combine within list of row data
        for item in range(len(row_data) - 1):
            if (item + 1) >= len(row_data):
                break
            if row_data[item] == row_data[item + 1]:
                row_data[item] = 2 * row_data[item + 1]
                row_data.pop(item + 1)
        
        # Put in placeholder spaces
        if (len(row_data) < 4):
            for amt in range(4 - len(row_data)):
                row_data.append('    ')
    
        # Update table_data
        for item in range(len(row_data)):
            table_data[item][column] = row_data[3 - item]

def move_left():
    print("LEFT")
    left_ok = toggle('left')
    
    # Repeat for each row
    for row in range(4):
        # Get the column data
        col_data = []
        for column in range(4):
            if table_data[row][column] != '    ':
                col_data.append(table_data[row][column])

        # Combine within list of row data
        for item in range(len(col_data) - 1):
            if (item + 1) >= len(col_data):
                break
            if col_data[item] == col_data[item + 1]:
                col_data[item] = 2 * col_data[item + 1]
                col_data.pop(item + 1)
        
        # Put in placeholder spaces
        if (len(col_data) < 4):
            for amt in range(4 - len(col_data)):
                col_data.append('    ')

        # Update table_data
        for item in range(len(col_data)):
            table_data[row][item] = col_data[item]

def move_right():
    print("RIGHT") 
    right_ok = toggle('right')

    # Repeat for each row
    for row in range(4):
        # Get the column data
        col_data = []
        for column in range(3, -1, -1):
            if table_data[row][column] != '    ':
                col_data.append(table_data[row][column])

        # Combine within list of row data
        for item in range(len(col_data) - 1):
            if (item + 1) >= len(col_data):
                break
            if col_data[item] == col_data[item + 1]:
                col_data[item] = 2 * col_data[item + 1]
                col_data.pop(item + 1)
        
        # Put in placeholder spaces
        if (len(col_data) < 4):
            for amt in range(4 - len(col_data)):
                col_data.append('    ')
        
        # Update table_data
        for item in range(len(col_data)):
            table_data[row][item] = col_data[3 - item]  

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

def toggle(choice):
    if choice == 'up' or choice == 'down':
        for column in range(4):
            row_data = []
            for row in range(4):
                if table_data[row][column] != '    ':
                    row_data.append(table_data[row][column])
            if len(row_data) < 4:
                return True
            for item in range(len(row_data) - 1):
                if row_data[item] == row_data[item + 1]:
                    return True
            return False

    if choice == 'left' or choice == 'right':
        for row in range(4):
            col_data = []
            for column in range(4):
                if table_data[row][column] != '    ':
                    col_data.append(table_data[row][column])
            if len(col_data) < 4:
                return True
            for item in range(len(col_data) - 1):
                if col_data[item] == col_data[item + 1]:
                    return True
            return False

        return False


def check_lose():
    up_ok = toggle('up')
    down_ok = toggle('down')
    right_ok = toggle('right')
    left_ok = toggle('left')

    if up_ok or down_ok or right_ok or left_ok:
        return
    else:
        print("You Lose!")
        exit()

def check_win():
    for row in table_data:
        if 2048 in row:
            print("You Win!")
            exit()

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

        check_lose()
        check_win()
        

if __name__ == "__main__":
    main()