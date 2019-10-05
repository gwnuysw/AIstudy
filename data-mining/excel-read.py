import xlrd

filename = "stats_104102.xls"

book = xlrd.open_workbook(filename)
sheet = book.sheet_by_index(0)
print(sheet)

data = []

for i in range(0,9):
    
