# Tile traveller, computer game
col = 1
line = 1
win = False
def options(col, line):
    if col == 1 and line == 1:
        result = "You can travel: (N)orth."
        return result
    if col == 1 and line == 2:
        result = "You can travel: (N)orth or (E)ast or (S)outh."
        return result
    if col == 1 and line == 3:
        return "You can travel: (E)ast or (S)outh."
    if col == 2 and line == 1:
        return "You can travel: (N)orth"
    if col == 2 and line == 2:
        return "You can travel: (S)outh or (W)est."
    if col == 2 and line == 3:
        return "You can travel: (E)ast or (W)est."
    if col == 3 and line == 1:
        return "You can travel: (N)orth."
    if col == 3 and line == 2:
        return "You can travel: (N)orth or (S)outh."
    if col == 3 and line == 3:
        return "You can travel: (S)outh or (W)est."

def new_line(direction, line):
    if direction == "n":
        line = line + 1
        return line
    if direction == "s":
        line = line -1
        return line
    if direction == "w":
        line = line
        return line
    if direction == "e":
        line = line
        return line

def new_col(direction, col):
    if direction == "n":
        col = col
        return col
    if direction == "s":
        col = col
        return col
    if direction == "w":
        col = col - 1
        return col
    if direction == "e":
        col = col + 1
        return col
    

while not win:
    options = options(col, line)
    print(options)
    direction = input("Direction: ")
    #direction = direction.lower()
    # if direction == "n" or direction == "e" or "s" or "w":
    #     print(1+1)
    # else:
    #     print(1)
    line = int(new_line(direction, line))
    col = int(new_col(direction,col))
    print(col)
    print(line)
