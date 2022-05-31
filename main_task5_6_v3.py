def greet():
    print("-------------------")
    print("  Hello Players!  ")
    print("  Here Simple TIC TAC TOE Game!  ")
    print("-------------------")
    print(" You should insert: coordinates x y ")
    print(" Where 'x' - row num  ")
    print(" Where 'y' - col num ")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    while True:
        cords = input("Please, go type: ").split()

        if len(cords) != 2:
            print(" Please, type 2 coordinates! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" You should insert digits! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Your coordinates is out of range ! ")
            continue

        if field[x][y] != " ":
            print(" oops! The sell already occupied! ")
            continue

        return x, y
def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("The 'X' is Winner!")
            return True
        if symbols == ["0", "0", "0"]:
            print("The '0' is Winner!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Now The X's turn to go")
    else:
        print("Now The 0's turn to go")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" That's a Draw!")
        break

