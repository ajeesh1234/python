import re
rule='[a-z_0-9]\w\W'+
s=input("enter")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")