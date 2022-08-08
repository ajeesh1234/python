# regular_expression..re
# pattern matching(string matching)
# for validation
# import re
# full match,finditer
# i.group..to search group
# i.start...to search where the match index


import re
count=0
matcher=re.finditer("ab","aaabaab")
for i in matcher:
    print(i.group())
    print(i.start())
    count=count+1
print(count)