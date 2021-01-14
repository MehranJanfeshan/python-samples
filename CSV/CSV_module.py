import csv

# Reading a CSV file

data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data, delimiter=',')

data_lines = list(csv_data)

print(data_lines[1])

# writing a CSV file
file_to_output = open('to_save_file.csv', mode='w', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

# Adding header
csv_writer.writerow(['a', 'b', 'c'])

# Adding rows
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()
