import re


iden_validator = re.compile(r"[a-z]{0,3}\d{2,8}[A-Z]{3,}$")

for _ in range(int(input())):
    if iden_validator.match(input()):
        print("VALID")
    else:
        print("INVALID")
