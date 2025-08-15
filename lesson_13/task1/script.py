import csv


def read_csv(file_name, delimiter):
    rows = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            rows.append(row)
    return rows


def remove_duplicates(rows):
    unique_rows = []
    seen = set()
    for row in rows:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)
    return unique_rows


def write_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)


random_data = read_csv('random.csv', ',')
rmc_data = read_csv('rmc.csv', ';')


unique_random = remove_duplicates(random_data)
unique_rmc = remove_duplicates(rmc_data)


all_unique_rows = unique_random + unique_rmc


write_csv('result_veliksar.csv', all_unique_rows)

