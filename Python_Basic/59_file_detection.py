

# Python file detection

import os


file_path = "text.txt"
# file path can be absolute (C:/Users/HP/Desktop/test.txt) or relative
# \t = Tab, so we can use "/" or "\\"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("The location does not exit")