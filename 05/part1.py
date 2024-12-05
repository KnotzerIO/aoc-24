import re
file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n\n')
rules, updates = file_content[0].split('\n'), file_content[1].split('\n')
if updates[-1] == '':
    updates.pop()

for rule in rules:
    before, after = rule.split('|')
    violation = r"{}(?:\s*,\s*\d+)*\s*,\s*{}".format(after, before)
    updates = [update for update in updates if not re.search(violation, update)]

sum = 0
for update in updates:
    update = update.split(',')
    sum += int(update[len(update) // 2])

print(sum)