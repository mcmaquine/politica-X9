import string
import PyPDF2
import tabula
import csv
import pandas as pd

#open pdf file and convert it to .csv, if it already exists do nothing
try:
    f = open('pdf.csv', 'x')
    df = tabula.convert_into("librev.pdf", "pdf.csv", output_format="csv")
except FileExistsError:
    print ('File Already Exists')

result = []
with open("pdf.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        result.append( row )

# find first item CNPJ
cnpj_i = 0
cnpj_j = 0
for row in result:
    inBreak = False # break row loop when item loop breaks
    cnpj_j = 0
    for item in row:
        if item == 'CNPJ':
            inBreak = True
            break
        cnpj_j+=1
    if inBreak: 
        break
    cnpj_i+=1

total_cnpj_item = 0
#find how many itens has column CNPJ
for iten in range( len(result) - cnpj_i ):
    try:
        if result[iten + cnpj_i][cnpj_j] == "":
            break
        else:
            total_cnpj_item += 1
            print(result[iten + cnpj_i][cnpj_j])
    except IndexError:
        break

print(result[cnpj_i].index("CNPJ"))

total_cnpj_item -= 1 #to no include CNPJ string count