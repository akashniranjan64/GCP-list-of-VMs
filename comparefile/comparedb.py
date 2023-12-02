import csv

def compare_csv(file1, file2):
    values_file1 = set()
    common_values = []

    with open(file1, 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            values_file1.add(tuple(row))

    with open(file2, 'r') as f2:
        reader = csv.reader(f2)
        for row in reader:
            if tuple(row) not in values_file1:
                common_values.append(row)
    return common_values

file1 = 'file1.csv'
file2 = 'file2.csv'
result = compare_csv(file1, file2)

if result:
    print("Common values:")
    for value in result:
        print(value)
else:
    print("No values found.")
