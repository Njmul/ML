
text = "Hello, This the first text that you will find inside the text file!"
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Wrote to demo.txt safely!")
