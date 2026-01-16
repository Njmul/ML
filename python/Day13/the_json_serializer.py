
import json

data = {"name": "Najmul", "age": 35, "skills": ["python", "sql"]}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved user as .json!")
