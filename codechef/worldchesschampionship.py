t=int(input())
for i in range(t):
    x=int(input())
    s=input()
    count=0
    found=0
    flag=0
    for i in s:
        if(i=="C"):
            count+=1
        elif(i=="N"):
            found+=1
        else:
            flag+=1
    countr=(2*count)+(1*flag)
    foundr=(2*found)+(1*flag)
    if(countr==foundr):
        print(55*x)
    elif(countr>foundr):
        print(60*x)
    else:
        print(40*x)