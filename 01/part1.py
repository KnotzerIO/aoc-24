file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read()

pairs = file_content.split('\n')
pairs.pop()

left_list = []
right_list = []

for pair in pairs:
    left, right = pair.split('   ')
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

distance = 0
for i in range(len(left_list)):
    distance += int(max(left_list[i], right_list[i])) - int(min(left_list[i], right_list[i]))

print(distance)