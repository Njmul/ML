
import csv

rows = []
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
print(reader)
print(rows)
