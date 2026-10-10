# Python writing files (.txt, .json, .csv)

# w > write
# x > write if file exit
# a > append
# r > read

# For text file
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
# txt_data = "I like pizza!"
# file_path= "output.txt"

# try:
#     with open(file=file_path, mode="a") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         # file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exit")





# For json file
# import os
# import json
# employee = {
#     "name": "Spongebob",
#     "age": "30",
#     "job": "cook"

# }


# txt_data = "I like pizza!"
# file_path= "output.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent= 4)

#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exit")



# For csv file


import json
import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrik", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]
file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already existed")


