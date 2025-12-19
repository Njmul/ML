data = input("Input a String: ")

frequency = {}
for i in data:

    if i in frequency:   # if single string is present in the frequency.
        frequency[i] += 1

    else:
        frequency[i] = 1 

print(frequency)


