import re
file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read()
real_mul = re.findall(r'mul\(\d+,\d+\)', file_content)
factors = [re.findall(r'\d+', mul) for mul in real_mul]

sum = 0
for factor in factors:
    sum += int(factor[0]) * int(factor[1])

print(sum)