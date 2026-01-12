

number = [2,-5,7,-4,5]

has_negative = any(x < 0 for x in number)
all_positive = all(x > 0 for x in number)

print(has_negative)
print(all_positive)
