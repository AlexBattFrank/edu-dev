def greet():
    print("-" * 17)
    print("  Hello Players!  ")
    print("  Here Simple TIC TAC TOE Game!  ")
    print("-" * 17)
    print(" You should insert: coordinates x 'space' y ")
    print(" Where 'x' - row num  ")
    print(" Where 'y' - col num ")


field = [["-"] * 3 for i in range(3)]

def show_field():
    print()
    print("    | 0 | 1 | 2 |")
    print("-" * 17)
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("-" * 17)
    print()


def req():
    while True:
        coord = input("          Please, go ahead!: ").split()
        if len(coord) != 2:
            print(" Please, type correct pair of coordinates!")
            continue

        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Please, input  a pair digits")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Coordinate(s) is out of range!")
            continue

        if field[x][y] != "-":
            print(" This cell is already occupied!")
            continue

        return x, y




def win_seq():
    win_coord = (((0, 0), (0, 1), (0, 2)),
                 ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)),
                 ((1, 0), (1, 1), (2, 1)),
                 ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)),
                 ((2, 0), (1, 1), (0, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("The 'X' is Winner!")
            return True
        if symbols == ["0", "0", "0"]:
            print("The '0' is Winner!")
            return True
    return False


greet()
field = [["-"] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Now The X's turn to go")
    else:
        print("Now The 0's turn to go")

    x, y = req()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_seq():
        break

    if count == 9:
        print(" That's a Draw!")
        break
