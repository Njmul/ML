def palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum()) # .isalnum() return false for space, symbols, punctuation and .lower() converts all into lower case.
    return cleaned == cleaned[::-1] # checking the palindrome

print(palindrome("My Name"))