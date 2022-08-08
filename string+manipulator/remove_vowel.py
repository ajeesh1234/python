# removal of vowels


s=input("enter a string")
n=""
for i in s:
    if i not in "aeiou":
        n=n+i
print(n)