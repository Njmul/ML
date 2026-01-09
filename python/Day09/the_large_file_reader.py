
def file(num_of_lines):
    for i in range(num_of_lines):
        yield f"line {i}"

for x in file(5):
    print(x)
