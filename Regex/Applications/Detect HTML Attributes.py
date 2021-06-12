import re, sys
from collections import defaultdict


finder = re.compile(r"<(\w+)(.*?)?>")
tags_finder = re.compile(r"\s([a-z]+)=")
subTags = finder.findall(sys.stdin.read())
Attributes = defaultdict(set)

for tag, attributes in subTags:
    Attributes[tag].update(tags_finder.findall(attributes))


for tag, attributes in sorted(Attributes.items()):
    print(tag, ':', ','.join(sorted(attributes)), sep='')
