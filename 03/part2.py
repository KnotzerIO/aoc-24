import re
file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read()

allowed = file_content.split("do()")
final_allowed= ""
for allowed in allowed:
     final_allowed +=  allowed.split("don't")[0]

real_mul = re.findall(r'mul\(\d+,\d+\)', final_allowed)
factors = [re.findall(r'\d+', mul) for mul in real_mul]

sum = 0
for factor in factors:
    sum += int(factor[0]) * int(factor[1])

print(sum)