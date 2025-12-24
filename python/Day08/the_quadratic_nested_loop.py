A = list(range(0,10000))
B = list(range(9999, 19999))
duplicates = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            duplicates.append(A[i])
            break

print("First 10 duplicates:", duplicates[0])