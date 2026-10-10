


# dictionary = a collection of { key: value} pairs
# ordered and changeable. No duplicates



capitals = { "USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))


if capitals.get("Japan"):
    print("That capital exist")
else:
    print("That capital does not exist")


# insert a  value pair
    
capitals.update({"Germany": "Berlin"})

# update a  value pair
capitals.update({"USA": "Detroit"})

# remove a  value pair
capitals.pop("China")

# remove a  value pair
capitals.popitem()


# remove all  value pair
capitals.clear()


keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(keys)


values = capitals.values()
print(values)
for value in capitals.values():
    print(values)


# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {values}")

