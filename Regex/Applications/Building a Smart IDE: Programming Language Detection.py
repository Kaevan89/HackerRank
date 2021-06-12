import re, sys


code = sys.stdin.read()
javaIdent = re.compile(r"static void main\(String\[\] args\)|java\.io")
CppIdent = re.compile(r"\#include<|int main\(\)\b\{")

if javaIdent.search(code):
    print ('Java')
elif CppIdent.search(code):
    print('C')
else:
    print('Python')
