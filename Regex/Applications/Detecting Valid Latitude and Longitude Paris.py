import re


validator = re.compile(r"\([+-]?(?:90(?:\.0+)?|[1-8][0-9](?:\.\d+)?|\d(?:\.\d+)?), [+-]?(?:180(?:\.0+)?|1[0-7]\d(?:\.\d+)?|[1-9]\d(?:\.\d+)?|\d(?:\.\d+)?)\)")

for _ in range(int(input())):
    pair = input()
    if(validator.match(pair)):
        print ("Valid")
    else:
        print ("Invalid")
