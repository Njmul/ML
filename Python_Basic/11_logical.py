# Logical operators = evaluate multiple conditions (or, and, not)

# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition ( not False, not True)


# OR
temp = 25
is_raining = True


if temp > 30 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")  

else:
    print("The outdoor event is still scheduled")



# AND

temp = 25
is_sunny = True


if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is Sunny")  

elif temp <=0 and is_sunny:
    print("It is Cold outside.")
    print("It is Sunny")

elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside.")
    print("It is Sunny") 
    
      
# NOT
elif temp >= 28 and not is_sunny:
    print("It is HOT outside.")
    print("It is Cloudy")  

elif temp <=0 and not is_sunny:
    print("It is Cold outside.")
    print("It is Cloudy")

elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside.")
    print("It is Cloudy") 


    