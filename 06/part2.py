file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n')
if file_content[-1] == '':
    file_content.pop()

guard = "^"
direction = "up"


def find_guard():
    coord = []
    for i in range(len(file_content)):
        if guard in file_content[i]:
            coord = [i, file_content[i].index(guard)]
    return coord


def move(pos, direction):
    if direction == "up":
        pos[0] -= 1
    elif direction == "down":
        pos[0] += 1
    elif direction == "left":
        pos[1] -= 1
    elif direction == "right":
        pos[1] += 1
    return pos


guard_pos = find_guard()
pos = [guard_pos[0] - 1, guard_pos[1]]

def check_for_infinity_loop(all_pos, file_content):
    pos = [guard_pos[0] - 1, guard_pos[1]]
    direction = "up"
    count = len(all_pos)
    while True:
        count += 1
        new_pos = move(pos.copy(), direction).copy()
        guard_did_leave = new_pos[0] < 0 or new_pos[0] >= len(file_content) or new_pos[1] < 0 or new_pos[1] >= len(
            file_content[0])
        if guard_did_leave:
            return False
        if count - len(all_pos) > 1000: # check for an infinity loop very inefficient but works
            return True
        if file_content[new_pos[0]][new_pos[1]] == "#" or file_content[new_pos[0]][new_pos[1]] == "O":
            if direction == "up":
                direction = "right"
            elif direction == "left":
                direction = "up"
            elif direction == "down":
                direction = "left"
            elif direction == "right":
                direction = "down"
        else:
            pos = new_pos
            all_pos.add(str(pos))

count_infinity = 0
for i in range(len(file_content)):
    for j in range(len(file_content[i])):
        if file_content[i][j] == "#" or file_content[i][j] == "^":
            continue
        all_pos = {str([i, j])}
        alt_file_content = file_content.copy()
        alt_file_content[i] = alt_file_content[i][:j] + "O" + alt_file_content[i][j+1:]
        if check_for_infinity_loop(all_pos, alt_file_content):
            count_infinity += 1


print(count_infinity)