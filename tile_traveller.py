# Tile traveller
# While the game is not won the programm will continue to ask for new directions
# A function will determine if the direction is valid
# if the direction is valid we move between tiles
# when we reach the winning tile the programm will stop
def game_loop(col, line):
    '''This function prints out the valid directions for each position'''
    if col == 1 and line == 1:
        result = "You can travel: (N)orth."
        return result
    if col == 1 and line == 2:
        result = "You can travel: (N)orth or (E)ast or (S)outh."
        return result
    if col == 1 and line == 3:
        result = "You can travel: (E)ast or (S)outh."
        return result
    if col == 2 and line == 1:
        result = "You can travel: (N)orth"
        return result
    if col == 2 and line == 2:
        result = "You can travel: (S)outh or (W)est."
        return result
    if col == 2 and line == 3:
        result = "You can travel: (E)ast or (W)est."
        return result
    if col == 3 and line == 1:
        result = "You can travel: (S)outh."
        return result
    if col == 3 and line == 2:
        result = "You can travel: (N)orth or (S)outh."
        return result
    if col == 3 and line == 3:
        result = "You can travel: (S)outh or (W)est."
        return result

def new_line(direction, line):
    '''This function finds the change in line for each move'''
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
    '''This function finds the change in collumn for each move'''
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

def valid_direction(direction,line,col):
    '''This function finds out if the direction that was entered is valid for the current position'''
    if col == 1 and line == 1 and direction != "n":
        valid = False
        return valid
    if col == 1 and line == 2:
        if direction != "n" and direction != "e" and direction != "s":
            valid = False
        return valid
    #eftir að klára fyrir rest
    if col == 1 and line == 3:
        result = "You can travel: (E)ast or (S)outh."
        return result
    if col == 2 and line == 1:
        result = "You can travel: (N)orth"
        return result
    if col == 2 and line == 2:
        result = "You can travel: (S)outh or (W)est."
        return result
    if col == 2 and line == 3:
        result = "You can travel: (E)ast or (W)est."
        return result
    if col == 3 and line == 1:
        result = "You can travel: (S)outh."
        return result
    if col == 3 and line == 2:
        result = "You can travel: (N)orth or (S)outh."
        return result
    if col == 3 and line == 3:
        result = "You can travel: (S)outh or (W)est."
        return result
    
# We start out in tile 1,1   
col = 1
line = 1
win = False
# While loop untill we get to the win tile
while not win:
    # We use the game_loop function to print put the options for the current position
    options = game_loop(col, line)
    print(options)
    direction = input("Direction: ")
    direction = direction.lower()
    # Use the valid_direction function to find out if the direction that was 
    # entered is valid for the current position
    valid =valid_direction(direction,line,col)
    # If the direction was valid, we move tiles
    if valid:
        line = int(new_line(direction, line))
        col = int(new_col(direction,col))
        print(col)
        print(line)
    else:
        print("Not a valid direction!")
    # What happens when you get to the victory location
    if line == 1 and col == 3:
        win = True
        print("Victory!")
