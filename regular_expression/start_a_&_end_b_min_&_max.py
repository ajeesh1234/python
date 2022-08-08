import re
rule='[a][\w\W]{3,6}[b]'
s=input("enter")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")