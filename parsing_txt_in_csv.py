import csv

file_book = open("pdf/test.txt", "r")

Master_Guide = open("pdf/Master_Guide.txt", "r")
Player_book = open("pdf/Player_book.txt", "r")
Rule_book = open("pdf/Rule_book.txt", "r")

with open("parsed_data/ALLItems.csv", newline="") as f:
    reader = csv.reader(f)
    ALLItems = list(reader)

with open("parsed_data/ammunition.csv", newline="") as f:
    reader = csv.reader(f)
    ammunition = list(reader)

with open("parsed_data/armor.csv", newline="") as f:
    reader = csv.reader(f)
    armor = list(reader)

with open("parsed_data/consumables.csv", newline="") as f:
    reader = csv.reader(f)
    consumables = list(reader)

with open("parsed_data/container.csv", newline="") as f:
    reader = csv.reader(f)
    container = list(reader)

with open("parsed_data/gear.csv", newline="") as f:
    reader = csv.reader(f)
    gear = list(reader)

with open("parsed_data/kit.csv", newline="") as f:
    reader = csv.reader(f)
    kit = list(reader)

with open("parsed_data/tool.csv", newline="") as f:
    reader = csv.reader(f)
    tool = list(reader)

with open("parsed_data/weapon.csv", newline="") as f:
    reader = csv.reader(f)
    weapon = list(reader)
# for i in file_book:
#     for j in data:
#         if j[1] in i:
#             print(i)