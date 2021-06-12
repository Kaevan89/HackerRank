import re, sys


comments_finder = re.compile(r"\/\/.+?(?=\n|$)|\/\*.+?\*\/", flags=re.DOTALL)
text = sys.stdin.read()
comments = comments_finder.findall(text)

for comment in comments:
    print(re.sub(r"\n +", r"\n", comment, flags=re.DOTALL))
