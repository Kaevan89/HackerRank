import re, sys


email_finder = re.compile(r"[\w.]+@[\w.]+\w+")
text = sys.stdin.read()
emails = list(set(email_finder.findall(text)))
emails.sort()
print(';'.join(emails))
