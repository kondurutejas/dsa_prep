t = int(input())
for i in range(t):
    s=input()
    a=int(s[0:2])
    b=int(s[3:5])
    if(a<=12 and b<=12):
        print("BOTH")
    elif(a<=31 and b<=12):
        print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")