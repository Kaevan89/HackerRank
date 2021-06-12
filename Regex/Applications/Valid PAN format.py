import re


validator = re.compile(r"[A-Z]{5}\d{4}[A-Z]$")

for _ in range(int(input())):
    
    if (validator.match(input())):
        print("YES")
    else:
        print("NO")
