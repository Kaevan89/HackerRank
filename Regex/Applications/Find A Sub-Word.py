import re

text = '\n'.join([input() for _ in range(int(input()))])
words = [input() for _ in range(int(input()))]
subwords = '|'.join(['\B' + word + '\B' for word in words])
subwords_finder = re.compile(subwords)
subwords_find = subwords_finder.findall(text)
for word in words:
    print(subwords_find.count(word))
