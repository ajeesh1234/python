import re
rule='[1][\w\W]{4}[0]'
s=input("enter")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")