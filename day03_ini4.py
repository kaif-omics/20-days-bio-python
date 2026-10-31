# Day 3: Rosalind INI4 - Conditions and Loops

a = 4638
b = 8780

sum = 0

for i in range (a, b+1):
    if i % 2 != 0:
        sum = sum + i

print(sum)