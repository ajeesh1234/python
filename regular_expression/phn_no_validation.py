# import re
# rule='\d{10}'
# s=input("enter phone number")
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

import re
rule='[+][9][1][0,9]{10}'
s=input("enter phone number")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")