def pallindrome(s):
    r=s[::-1]
    if s==r:
        return("pallindrome")
    else:
        return("not pallindrome")
print(pallindrome("malayalam"))
print(pallindrome("abc"))