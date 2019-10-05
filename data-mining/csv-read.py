import codecs

filename = "list-euckr.csv"
csv = codecs.open(filename, "r", "utf-8").read()

data = []
rows = csv.split("\n")
print("rows ", rows)
for row in rows:
    print("row ", row)
    if row == "": continue
    cells = row.split(",")
    print("cells ", cells)
    data.append(cells)

for c in data:
    print(c[1], c[2])
