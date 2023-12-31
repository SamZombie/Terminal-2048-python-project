from random import randint

line1 = [0,0,0,0]
line2 = [0,0,0,0]
line3 = [0,0,0,0]
line4 = [0,0,0,0]

def print_lines():
    all_lines = [line1,line2,line3,line4]
    for line in all_lines:
        line_str = ''
        for number in line:
            space_len = ' ' * (5 - len(str(number)))
            line_str += str(number)
            line_str += space_len
        print(line_str)

def test_fail():
    global line1
    global line2
    global line3
    global line4
    if (0 not in line1) and (0 not in line2) and (0 not in line3) and (0 not in line4):
            line1_c = line1
            line2_c = line2
            line3_c = line3
            line4_c = line4
            push_rows()
            push_rows(True)
            push_columns()
            push_columns(True)
            if (line1_c != line1) or (line2_c != line2) or (line3_c != line3) or (line4_c != line4):
                line1 = line1_c
                line2 = line2_c
                line3 = line3_c
                line4 = line4_c
            else: player1.fail = True

def point_in_line(line, tile):
    while 0 in line:
        rand_point = randint(0,3)
        if (line[rand_point] == 0):
            line[rand_point] = tile
            break

def new_tile():
    tile = randint(1,10)
    if (tile == 10):
        tile = 4
    else: tile = 2
    rand_line = randint(1,4)
    if (rand_line == 1) and (0 in line1):
        point_in_line(line1, tile)
    elif (rand_line == 2) and (0 in line2):
        point_in_line(line2, tile)
    elif (rand_line == 3) and (0 in line3):
        point_in_line(line3, tile)
    elif (rand_line == 4) and (0 in line4):
        point_in_line(line4, tile)
    else: new_tile()

def push_direction(coro, invert):
    if invert:
        coro.reverse()
    pushed_row = []
    compact_row = []
    n = 0
    for i in list(range(4)):
        if coro[i] != 0:
          pushed_row.append(coro[i])
        else: n += 1
    pushed_row += ([0] * n)
    if pushed_row[0] == 0:
        compact_row = pushed_row
    elif (pushed_row[0] == pushed_row[1]) and (pushed_row[2] == pushed_row[3]):
        compact_row = [(pushed_row[0]*2), (pushed_row[2]*2), 0, 0]
        player1.points += pushed_row[0]*2
        player1.points += pushed_row[2]*2
    elif pushed_row[0] == pushed_row[1]:
        compact_row = [(pushed_row[0]*2), pushed_row[2], pushed_row[3], 0]
        player1.points += pushed_row[0]*2
    elif pushed_row[2] == pushed_row[3]:
        compact_row = [pushed_row[0], pushed_row[1], (pushed_row[2]*2), 0]
        player1.points += pushed_row[2]*2
    elif pushed_row[1] == pushed_row[2]:
        compact_row = [pushed_row[0], (pushed_row[1]*2), pushed_row[3], 0]
        player1.points += pushed_row[1]*2
    else: compact_row = pushed_row
    if invert:
        coro.reverse()
        compact_row.reverse()
    return compact_row

def push_rows(right = False):
    global line1
    global line2
    global line3
    global line4
    line1 = push_direction(line1, right)
    line2 = push_direction(line2, right)
    line3 = push_direction(line3, right)
    line4 = push_direction(line4, right)

def push_columns(down = False):
    global line1
    global line2
    global line3
    global line4
    pushed_column = []
    for i in [0,1,2,3]:
        n = push_direction([line1[i], line2[i], line3[i], line4[i]], down)
        pushed_column.append(n)
    line1 = [pushed_column[0][0], pushed_column[1][0], pushed_column[2][0], pushed_column[3][0]]
    line2 = [pushed_column[0][1], pushed_column[1][1], pushed_column[2][1], pushed_column[3][1]]
    line3 = [pushed_column[0][2], pushed_column[1][2], pushed_column[2][2], pushed_column[3][2]]
    line4 = [pushed_column[0][3], pushed_column[1][3], pushed_column[2][3], pushed_column[3][3]]
    
    

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.fail = False

def gameplay():
    global line1
    global line2
    global line3
    global line4
    line1_c = line1
    line2_c = line2
    line3_c = line3
    line4_c = line4
    print_lines()
    move = input("input: ")
    if move == 'exit':
        player1.fail = True
    if move == 'w' or move == 'W':
        push_columns()
    elif move == 'a' or move == 'A':
        push_rows()
    elif move == 's' or move == 'S':
        push_columns(True)
    elif move == 'd' or move == 'D':
        push_rows(True)
    else: pass
    if (line1_c != line1) or (line2_c != line2) or (line3_c != line3) or (line4_c != line4):
        new_tile()
        test_fail()

        

name = input("Welcome to 2048, to begin please type in your name! ")
player1 = Player(name)
new_tile()
new_tile()
print('')
print('Press w to move up, a to move left, s to move down, and d to move right')
while player1.fail is False:
    gameplay()
print_lines()
print("Game Over, your score is:")
print(player1.points)
