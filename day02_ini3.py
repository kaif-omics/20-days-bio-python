# Day 2: Rosalind INI3 - Strings and Slicing

dna_text = "WtSCaoDbJM9CqC13a14ULdmLHRJg4U4Bq04LMyL3azLNQNOj6so9OfexBIOr0Ot6GlN4f8s0Nn48549PpucmVqLpfKcCiMegapterahzmEJoEhapUhqqiqvfhQ2CSkScJkD6KJdVPiVkVz2KEmxfNmslX8xRbolsY6barbatusCadmBTZqg542pMsWIbOpt"

a = 93 
b = 101
c = 162
d = 169

first_word = dna_text[a:b+1]
second_text = dna_text[c:d+1]

print(first_word, second_text)