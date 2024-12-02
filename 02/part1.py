file_path = 'input'

safe = 0
with open(file_path, 'r') as file:
    for line in file:
        is_row_safe = True
        row = [int(item) for item in line.strip().split()]
        print(row)
        if row == sorted(row) or row == sorted(row, reverse=True):
            for i in range(len(row)):
                if i > 0:
                    adjacent = [int(row[i - 1]), int(row[i])]
                    difference = max(adjacent) - min(adjacent)
                    if not (0 < difference <= 3):
                        is_row_safe = False
                        break
        else:
            is_row_safe = False
        if is_row_safe:
            print('Row is safe')
            safe += 1

print(safe)