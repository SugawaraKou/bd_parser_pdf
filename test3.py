import os
import csv

#a = 146
#os.system("pdftotext -f " + str(a) + " -l " + str(a) + " -layout pdf/test.pdf")
# reader_object = csv.reader("parsed_data/armor.csv", delimiter=",")
#
# file_book = open('pdf/test.txt', 'r')
# reader_object = csv.reader("parsed_data/armor.csv", delimiter=",")
# csv_iter = csv.reader('parsed_data/armor.csv')
#
#
# for i in file_book:
#     for u in csv_iter:
#         if u in i:
#             print("OK")

file_book = open("pdf/test.txt", "r")

with open("parsed_data/armor.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

for i in file_book:
    for j in data:
        if j[1] in i:
            print(i)