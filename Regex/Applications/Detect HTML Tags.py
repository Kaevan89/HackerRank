import re, sys

html_text = sys.stdin.read()
tag_finder = re.compile(r"<\s*([a-z0-9]+)")
tags = set(tag_finder.findall(html_text))
tags = list(tags)
print(';'.join(sorted(tags)))
