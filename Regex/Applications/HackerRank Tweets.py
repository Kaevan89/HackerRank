import re


HackerRank = re.compile(r"hackerrank", flags=re.IGNORECASE)
cont = 0

for _ in range(int(input())):
    
    if HackerRank.search(input()):
        cont += 1

print(cont)
