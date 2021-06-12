import re, sys


text = sys.stdin.read()
scraper = re.compile(r'<div class="summary">.+?"\/questions\/(\d+.)\/.+?>(.+?)<.+?"relativetime">(.+?)<', flags=re.DOTALL | re.IGNORECASE)
scraps = scraper.findall(text)

for scrap in scraps:
    print(';'.join(scrap))
