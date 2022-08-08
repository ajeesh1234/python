
def pallindrome(s):
    r=s[::-1]
    if s==r:
        print("pallindrome")
    else:
        print("not pallindrome")
pallindrome("malayalam")
pallindrome("abc")