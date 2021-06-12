import re, sys

html_text = sys.stdin.read()
html_finder = re.compile(r'<a href="(.*?)".*?>([A-Za-z0-9 ,./]*)(?=</)')
matches = html_finder.findall(html_text)

for match in matches:
    link, description = match
    print('{},{}'.format(link.strip(), description.strip()))
