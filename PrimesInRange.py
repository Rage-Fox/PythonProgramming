n1=int(input())
n2=int(input())
s=1
if(n1>n2):
    s=-1
for i in range(n1,n2+s,s):
        for j in range(2,int(i**0.5)+1):
                if(i%j==0):
                        break

        else:
                print(i,end=" ")
