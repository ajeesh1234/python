def fibinocci(nterms):
    n1=0
    n2=1
    for i in range(nterms):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
fibinocci(20)
