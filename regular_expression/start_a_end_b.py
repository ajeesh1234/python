import re
rule='[a][\w\W]*[b]'
s=input("enter")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")