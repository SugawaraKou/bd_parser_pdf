import os
import time

start = 247
end = 269
os.system("pdftotext -f " + str(start) + " -l " + str(end) + " -layout pdf/Master_Guide.pdf")
time.sleep(10)
print("Parsing pdf/Master's_Guide: OK")
start = 146
end = 159
os.system("pdftotext -f " + str(start) + " -l " + str(end) + " -layout pdf/Player_book.pdf")
time.sleep(10)
print("Parsing pdf/Player_book.pdf: OK")
start = 16
end = 19
os.system("pdftotext -f " + str(start) + " -l " + str(end) + " -layout pdf/Rule_book.pdf")
time.sleep(10)
print("Parsing pdf/Rule_book.pdf: OK")