

class Board:
    my_board = ['', '', '', '', '', '', '', '', '']
    def print_current_status(status):
        for i, cell in enumerate(status):
            if (i + 1) % 3 == 0:
                print(f'{cell}')
            else:
                print(f'{cell}|', end='')

    print_current_status(my_board)