fixed_amount=100000
amount=int(input("enter amount"))
if amount>fixed_amount:
    print("insufficient")
else:
    print("balance amount is:",fixed_amount-amount)