


# Python reading files (.txt, .csv, .json)

# For .txt file
# file_path = "output.txt"
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")

# except PermissionError:
#     print("You do not have permission to read that file")


# For  .json file
    

import json

file_path = "output.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")




# For  .csv file
    

import csv

file_path = "output.json"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        print(content[0])
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")


# Different Approach
import csv

file_path = "output.json"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")