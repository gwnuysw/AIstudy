import pandas as pd

filename = "stats_104102.xls"

book = pd.read_excel(filename, header=2)

print(book)
