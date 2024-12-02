file_path = 'input'

def is_safe(row):
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row)):
            if i > 0:
                adjacent = [int(row[i - 1]), int(row[i])]
                difference = max(adjacent) - min(adjacent)
                if not (0 < difference <= 3):
                    return False
    else:
        return False
    return True

safe = 0
with open(file_path, 'r') as file:
    for line in file:
        row = [int(item) for item in line.strip().split()]
        if is_safe(row):
            safe += 1
        else:
            is_other_safe = False
            for i in range(len(row)):
                alternate = row.copy()
                alternate.pop(i)
                if is_safe(alternate):
                    is_other_safe = True
                    break
            if is_other_safe:
                safe += 1

print(safe)