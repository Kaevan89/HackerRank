import re


class IP_validator:

    #byte_8 = r"([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])"
    #byte_16 = r"[a-fA-F\d]{1,4}"
    IPv4 = re.compile(r"(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?:\.(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])){3}$")
    IPv6 = re.compile(r"[a-fA-F\d]{1,4}(?::[a-fA-F\d]{1,4}){7}$")

    def validate(self, IP):

        if (self.IPv4.match(IP)):
            return "IPv4"

        if (self.IPv6.match(IP)):
            return "IPv6"

        return "Neither"


validator = IP_validator()

for _ in range(int(input())):
    print(validator.validate(input()))
