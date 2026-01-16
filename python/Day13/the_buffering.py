

with open("big_file.txt", "w", encoding="utf-8") as f:

    for i in range(1000000):
        f.write(f"Line {i}\n")

print("Writing of 1,000,000 lines just completed")



