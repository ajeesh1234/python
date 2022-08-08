# import re
# rule='a+'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='a*'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='a?'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='a{2}'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='a{2,3}'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='^a'
# count=0
# matcher=re.finditer(rule,"aaa abc aaaa @123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

import re
rule='a$'
count=0
matcher=re.finditer(rule,"aaa abc aaaa @123")
for i in matcher:
    print(i.group())
    print(i.start())
    count=count+1
print(count)