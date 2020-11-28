import pandas as pd

Master_Guide = open("pdf/test.txt", "r")
Master_Guide = Master_Guide.readlines()
print(Master_Guide)
#print(Master_Guide.readlines())
flag = False
for i in Master_Guide:
    if i == "\n":
        flag = True
    if flag == True:
        print(i)