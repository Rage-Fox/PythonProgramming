a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
#set poperties have to be used only on sets itself
#conversion of list into set is compulsory
a=set(a)
b=set(b)
print(a.union(b))#set property
print(a.intersection(b))#set property
print(a.difference(b))#unique elements in a #a-b
print(b.difference(a))#unique elements in b #b-a

