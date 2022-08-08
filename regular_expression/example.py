# import re
# rule='[abc]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='[^abc]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)


# import re
# rule='[a-z]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='[abc]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='[a-zA-Z]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

# import re
# rule='[0-9]'
# count=0
# matcher=re.finditer(rule,"abc @KABW123")
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

import re
rule='[^0-9a-zA-Z]'
count=0
matcher=re.finditer(rule,"abc @KABW123")
for i in matcher:
    print(i.group())
    print(i.start())
    count=count+1
print(count)