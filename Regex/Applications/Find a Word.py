import re

# Maybe in the future you should make everything tiny
text = '\n'.join([input() for _ in range(int(input()))])
words = [input() for _ in range(int(input()))]
words_reg = '|'.join(['(?:(?<=\W)|^)' + word + '(?=\W|$)' for word in words])
words_finder = re.compile(words_reg)
words_find = words_finder.findall(text)

for word in words:
    print(words_find.count(word))
