import PyPDF2
import tabula
import csv

try:
    f = open('pdf.csv', 'x')
    df = tabula.convert_into("librev.pdf", "pdf.csv", output_format="csv")
except FileExistsError:
    print ('File Already Exists')

# in order to print first 5 lines of Table

with open('pdf.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')