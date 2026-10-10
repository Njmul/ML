

#format specifiers = {value : flags} format a value based on what
#  flags are inserted


# . (number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many species
# :03 = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator



price1 = 3.14159
price2 = -987.56
price3 = 12.34

# . (number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")


# : (number) = allocate that many species
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")


# :03 = allocate that many spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")


# :< = left justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")



# :> = right justify
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")


# :^ = center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# :+ = use a plus sign to indicate positive value
print(f"Price 1 is ${price1:+10}")
print(f"Price 2 is ${price2:+10}")
print(f"Price 3 is ${price3:+10}")

# :  = insert a space before positive numbers

# :, = comma separator
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


# Combination
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")