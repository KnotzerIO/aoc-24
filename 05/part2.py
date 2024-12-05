import re

file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n\n')
rules, updates = file_content[0].split('\n'), file_content[1].split('\n')
if updates[-1] == '':
    updates.pop()

def is_valid(update):
    for rule in rules:
        before, after = rule.split('|')
        violation = r"{}(?:\s*,\s*\d+)*\s*,\s*{}".format(after, before)
        if re.search(violation, update):
            return False
    return True

def reorder_update(update):
    pages = update.split(',')
    ordered_pages = []
    while pages:
        for page in pages:
            valid = True
            for rule in rules:
                before, after = rule.split('|')
                if page == after and before in pages: #
                    valid = False
                    break
            if valid:
                ordered_pages.append(page)
                print(ordered_pages)
                pages.remove(page)
                break
    return ','.join(ordered_pages)

invalids = []
for update in updates:
    if not is_valid(update):
        invalids.append(reorder_update(update))

sum_invalids = 0
for update in invalids:
    update = update.split(',')
    sum_invalids += int(update[len(update) // 2])

print(sum_invalids)