initial=int(input("enter intial range"))
final=int(input("enter final range"))
sum=0
while initial<=final:
    if initial%2==0:
        sum=initial+sum
    initial=initial+1
print(sum)