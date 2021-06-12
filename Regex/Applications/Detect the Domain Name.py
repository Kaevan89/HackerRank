import re
from sys import stdin


text = stdin.read()
domain_finder = re.compile(r"""(?:https?:\/\/(?:ww[w2]\.)?)([A-Za-z0-9.-]+\.[A-Za-z0-9-]+)(?=\/|_|\?|"|'|\\|\s|$)""")
all_domains = list(set(domain_finder.findall(text)))
all_domains.sort()
print(';'.join(all_domains))
