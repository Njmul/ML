
# Indexing = accessing elements of a sequence using [] (indexing operator)

# [start : end : step]


credit_number = "1234-5678-9866-7688"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[ :4])
print(credit_number[ 5: 9])
print(credit_number[ 5: ])
print(credit_number[-2])
print(credit_number[ : : 2])
print(credit_number[0])


# Print last four digits
last_digits = credit_number[-4:]
print(last_digits) 


# For reversing the digits
credit_number =credit_number[ : :-4]
print(credit_number)