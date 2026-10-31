# Day 4: Rosalind INI5 - Working with Files

with open ("rosalind_ini5.txt", "r") as file:
    lines = file.readlines()

even_line = lines[1::2]

for line in even_line:
    print(line.strip())
