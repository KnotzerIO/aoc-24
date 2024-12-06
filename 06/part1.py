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
all_pos = {str(guard_pos), str(pos)}
while True:
    new_pos = move(pos.copy(), direction)
    guard_did_leave = new_pos[0] < 0 or new_pos[0] >= len(file_content) or new_pos[1] < 0 or new_pos[1] >= len(file_content[0])
    if guard_did_leave:
        break

    if file_content[new_pos[0]][new_pos[1]] == "#":
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

print(len(all_pos))

