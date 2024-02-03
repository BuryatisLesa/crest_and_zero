def check_winner(board, char):
    """Функция условий определение победителя"""
    # Проверка строк!
    if all((board[0][0] == char, board[0][1] == char, board[0][2] == char)):
        return char
    if all((board[1][0] == char, board[1][1] == char, board[1][2] == char)):
        return char
    if all((board[2][0] == char, board[2][1] == char, board[2][2] == char)):
        return char
    # Проверка столбцов!
    if all((board[0][0] == char, board[1][0] == char, board[2][0] == char)):
        return char
    if all((board[0][1] == char, board[1][1] == char, board[2][1] == char)):
        return char
    if all((board[0][2] == char, board[1][2] == char, board[2][2] == char)):
        return char
    # Проверка по диагонали!
    if all((board[0][0] == char, board[1][1] == char, board[2][2] == char)):
        return char
    if all((board[2][0] == char, board[1][1] == char, board[0][2] == char)):
        return char
    else:
        return None


def select_win(char):
    """Функция вывода победителя и конца игры!"""
    if char == 'X':
        print('Победили кресты!')
        return False
    elif char == '0':
        print('Победили нули!')
        return False
    else:
        return True


def step_game(var, player):
    """Функция хода игры!"""
    player_step = True
    while player_step:
        print(f'Ход: {player}ов')
        board_cord_column = int(input('Введите номер столбца: ')) - 1
        board_cord_row = int(input('Введите номер строки: ')) - 1
        if 0 <= board_cord_row and board_cord_column <= 2:
            if main[board_cord_row][board_cord_column] == '*':
                main[board_cord_row][board_cord_column] = var
                print(f'Ваш ход - column: {board_cord_column + 1}, row: {board_cord_row + 1}')
                player_step = False
                for print_func in main:
                    print(print_func)
            elif main[board_cord_row][board_cord_column] == '0':
                print(f'Эта ячейка занята ноликами!')
            elif main[board_cord_row][board_cord_column] == 'X':
                print(f'Эта ячейка занята крестиками!')
        else:
            print('Ваши координаты выходит за диапазон поля\n'
                  'Диапазон координат от 1 до 3!')


map_1 = []
main_map = []
for i in range(3):
    map_1.append('*')
for j in range(3):
    main_map.append(map_1.copy())
game = True
while game:
    print('Добро пожаловать!\n', 'Игра "Крестики и Нолики"')
    main = main_map.copy()
    for i_1 in main:
        print(i_1)
    print('Игра началась, Вы играете за крестики, сделайте первый ход!')
    while game:
        step_game('X','Крестик')
        if not select_win(check_winner(main,'X')):
            game = False
        else:
            step_game('0','Нолик')
            if not select_win(check_winner(main, '0')):
                game = False
