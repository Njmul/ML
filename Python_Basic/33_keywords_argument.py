

# keyword argument =  an argument precede by an identifier
#                       helps with readability
#                       order of arguments doesn't matter
#                       1. Positional 2. default 3. KEYWORD 4. arbitrary


# Example 1: 
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello!", "Mr.", "Luke", "Ducker")

hello("Hello!", title="Mr.", first="Luke", last="Ducker")

hello("Hello!", first="Luke", last="Ducker", title="Mr.")

# Example 2: 
# This will not work.
hello(first="Luke", last="Ducker", title="Mr.","Hello!")


for x in range(1, 11):
    print(x, end =" ")

# Example 3: 
print("1", "2", "3", "4", "5", sep="-")

# Example 4: 


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7898)
