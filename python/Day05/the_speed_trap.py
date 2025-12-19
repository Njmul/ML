a_list = list(range(1000000))
checking_number = -1
hash_table = set(a_list)

exist_in_list= checking_number in a_list
exist_in_hash_table= checking_number in hash_table

print(exist_in_list)
print(exist_in_hash_table)
