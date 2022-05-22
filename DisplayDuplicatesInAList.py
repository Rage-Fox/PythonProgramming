n=int(input())
arr=list(map(int,input().split()))
brr=[]
for i in arr:
    if i not in brr and arr.count(i)>1:
        brr.append(i)
print("There are "+str(len(brr))+" duplicate elements in the input array")
print(*brr)
