import re
rule='[+][9][1]\d{10}'
f=open("phone.txt",'r')
for i in f:
    number=i.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher is not None:
        print(number)