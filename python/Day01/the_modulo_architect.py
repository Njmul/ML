seconds = int(input("Enter a number in seconds"))
print(f"seconds {seconds}")

hours = seconds//3600
print(f"hours {hours}")

minutes = (seconds % 3600) // 60
print(f"minutes {minutes}")

remaining_seconds = float((((seconds % 3600) / 60)-minutes)*60)
print(f"remaining seconds {remaining_seconds}")
