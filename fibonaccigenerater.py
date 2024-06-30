n=int(input("Enter the number"))
n0=0
n1=1
print(n0,n1,end='')
for i in range (n):
    n2=n1+n0
    print(n2,end='')
    n0=n1
    n1=n2