from pathlib import Path

folder = Path("logs")
filename = "app.log"

path = folder/filename
print(path)

path.parent.mkdir(parents=True, exist_ok=True) # Making a folder if it doesn't exist.
path.write_text("Hello\n", encoding="utf-8")
