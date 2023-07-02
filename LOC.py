i=1
while (i<=1000):
    print('test case',i,':\n')
    num=input("enter number:")
    s=str(num)
    ls=list(s)
    ls[0],ls[4]=ls[4],ls[0]
    new_s="".join(ls)
    new_num=int(new_s)
    print(new_num)
    i=i+1
