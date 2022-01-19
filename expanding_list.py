# expanding number
x=list(map(int,input().split()))
t=abs(x[0]-x[1])
for i in range(2,len(x)):
    if abs(x[i]-x[i-1])>t:
       t= abs(x[i]-x[i-1])
    else:
       print("False")
       break
else:
    print("True")
