import re
rule='[a-zA-Z]{5}'
s=input("enter")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")