import random
for i in range(5):
    print(random.random(),end=" ")#in between 0 and 1(decimals)
    #random is module and .random is a function
    print(random.uniform(1,10),end=" ")#desired range
    print(random.randint(1,5),end=" ")#only integers '''including both the boundaries'''
    print(random.randrange(1,100,2))#excludes upperlimit, works exaxctly like a for loop
a=['c','c++','python','java','golang','c#','ruby']
#we cannot generate strings randomly using random module but we can select random from existing list
for i in range(5):
    print(random.choice(a))
    print(random.sample(a,2))#random combination of list elements and output is a list
print(a)
random.shuffle(a)#modifies the list
print("After some random shuffling:",a)
