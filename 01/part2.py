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

similarity_score = 0
for i in range(len(left_list)):
    appearances = right_list.count(left_list[i])
    similarity_score += appearances * int(left_list[i])

print(similarity_score)