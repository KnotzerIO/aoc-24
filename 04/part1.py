file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n')
    if file_content[-1] == '':
        file_content.pop()

xmas = "XMAS"
def check_horizontal(file_content):
    appear = 0
    for line in file_content:
        appear += line.count(xmas)
        appear += line.count(xmas[::-1])
    return appear

def check_vertical(file_content):
    vertical = []
    for i in range(len(file_content)):
        vertical.append(''.join([line[i] for line in file_content]))
    appear = 0
    for line in vertical:
        appear += line.count(xmas)
        appear += line.count(xmas[::-1])
    return appear

def check_diagonal_right(file_content):
    appear = 0
    for i in range (len(file_content)- len(xmas) +1):
        for j in range (len(file_content[i])- len(xmas) + 1):
            diagonal_word = file_content[i][j] + file_content[i+1][j+1] + file_content[i+2][j+2] + file_content[i+3][j+3]
            if xmas == diagonal_word or xmas == diagonal_word[::-1]:
                appear += 1
    return appear

def check_diagonal_left(file_content):
    file_content = [line[::-1] for line in file_content]
    return (check_diagonal_right(file_content))


def check_for_xmas(file_content):
    appear = 0
    appear += check_horizontal(file_content)
    appear += check_vertical(file_content)
    appear += check_diagonal_right(file_content)
    appear += check_diagonal_left(file_content)
    return appear

print(check_for_xmas(file_content))
