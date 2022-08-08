# KL02AV4545KL02AV4545

import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
s=input("enter vehicle number")
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("invalid")