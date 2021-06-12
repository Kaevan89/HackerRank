import re


API_ident = re.compile(r"^[1-9]\d{4} (?:C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$")

for _ in range(int(input())):
    if API_ident.match(input()):
        print ("VALID")
    else:
        print ("INVALID")
