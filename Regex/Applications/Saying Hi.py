import re


reg_hi = re.compile(r"[Hh][iI] [^Dd].+")

for _ in range(int(input())):
    
    string = input()
    if reg_hi.match(string):
        print(string)
