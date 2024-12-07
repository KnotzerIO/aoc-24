file_path = 'input'
from itertools import product
import re
with open(file_path, 'r') as file:
    file_content = file.read().split('\n')

if file_content[-1] == '':
    file_content.pop()

symbols = ['+', '*']

def calculate(eq):
    sum = 0
    nums = re.findall(r'\d+', eq)
    ops = re.findall(r'[\+\*]', eq)
    for i in range(len(nums)):
        if i == 0:
            sum = int(nums[i])
        else:
            if ops[i-1] == '+':
                sum += int(nums[i])
            elif ops[i-1] == '*':
                sum *= int(nums[i])
    return sum

total_calibration_result = 0
for line in file_content:
    value, equation = line.split(": ")
    op_count = equation.count(" ")
    combos = product(symbols, repeat=op_count)
    for combo in combos:
        new_eq = equation
        for op in combo:
            new_eq = new_eq.replace(" ", op ,1)
        if calculate(new_eq) == int(value):
            total_calibration_result += int(value)
            break

print(total_calibration_result)



