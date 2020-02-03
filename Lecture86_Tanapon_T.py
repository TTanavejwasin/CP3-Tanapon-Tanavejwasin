import csv

def readCSV():
    with open('File.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{"".join(row)}')
                line_count += 1
            else:
                print(f'{row[0]}{row[1]}{row[2]}')
                line_count += 1
        print(f'Processed {line_count} lines.')

readCSV()