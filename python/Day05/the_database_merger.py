defaults = {"theme": "light", "audio": "on"}

user_pref = {"theme" : "dark"}

merged = defaults.copy() # copy the value of the dictionaries not the address

merged.update(user_pref) # overrides the value of "merged" with the value of "user_pref"

print(merged)