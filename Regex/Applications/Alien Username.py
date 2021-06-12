import re

valid_username = re.compile(r"[_.]\d+[a-zA-Z]*_?$")

for _ in range(int(input())):
    username = input()
    if valid_username.match(username):
        print("VALID")
    else:
        print("INVALID")
