

text = "Hello, This the first text that you will find inside the text file!\n"
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Wrote to demo.txt safely!")


log_line = "this is the new line that i want to add as append\n"
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write(log_line)
print("New line added after append")
