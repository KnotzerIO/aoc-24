file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n')
    if file_content[-1] == '':
        file_content.pop()

mas = "MAS"


def get_diagonal_right(file_content):
    diagonals = []
    for i in range(len(file_content) - len(mas) + 1):
        for j in range(len(file_content[i]) - len(mas) + 1):
            diagonal_word = file_content[i][j] + file_content[i + 1][j + 1] + file_content[i + 2][j + 2]
            diagonals.append(diagonal_word)
    return diagonals


def get_diagonal_left(file_content):
    diagonals = []
    for i in range(len(file_content) - len(mas) + 1):
        for j in range(len(file_content[i]) - len(mas) + 1):
            diagonal_word = file_content[i][j + 2] + file_content[i + 1][j + 1] + file_content[i + 2][j]
            diagonals.append(diagonal_word)
    return diagonals


pairs = []
rights, lefts = get_diagonal_right(file_content), get_diagonal_left(file_content)

for i in range(len(rights)):
    pairs.append([rights[i], lefts[i]])


count = 0
for pair in pairs:
    if (pair[0] == mas or pair[0] == mas[::-1]) and (pair[1] == mas or pair[1] == mas[::-1]):
        count += 1

print(count)
