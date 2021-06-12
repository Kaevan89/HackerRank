import re


hackerRank1 = re.compile(r"^(?:hackerrank)", flags=re.IGNORECASE)
hackerRank2 = re.compile(r"(?:hackerrank)$", flags=re.IGNORECASE)
hackerRank3 = re.compile(r"^(?:hackerrank)$|^(?:hackerrank).+(?:hackerrank)$", flags=re.IGNORECASE)

for _ in range(int(input())):
    string = input()
    if hackerRank3.search(string):
        print(0)
    elif hackerRank2.search(string):
        print(2)
    elif hackerRank1.search(string):
        print(1)
    else:
        print(-1)
