import re


text = '\n'.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    a_word = input()
    b_word = a_word[:-2] + 'se'
    print(len(re.findall(rf"\b{a_word}\b|\b{b_word}\b", text)))
