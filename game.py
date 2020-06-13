from terminaltables import SingleTable

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
    return table_instance.table

def draw_grid_init():
    table_data = [
        ['    ', '    ', '    ', '    '],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ]
    table_instance = SingleTable(table_data, 'Play Game')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center'}
    return table_instance.table

def main():
    print(draw_grid())
    print("DONE")
    print(draw_grid_init())
    print("OK")

if __name__ == "__main__":
    main()