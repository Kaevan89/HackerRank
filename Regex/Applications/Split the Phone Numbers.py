import re


phone_numeber = re.compile(r"(?P<CountryCode>\d{1,3})[ -](?P<LocalAreaCode>\d{1,3})[ -](?P<Number>\d{4,10})")

for _ in range(int(input())):
    match = phone_numeber.match(input())
    phone = match.groupdict()
    print('CountryCode', '=', phone['CountryCode'], ',', 'LocalAreaCode', '=', phone['LocalAreaCode'], ',', 'Number', '=', phone['Number'], sep='')
