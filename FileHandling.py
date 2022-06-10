a=open(r'E:\\T-Hub\\2nd Semester\\Python Programming\\example.txt','w')
'''
x-> create
r-> read #read just reads the content and also doesn't create the file
w-> create and write #write mode overwrites the old content and also creates file even if it is not there
a-> create and append #appends everything without overwriting and also can create a file even if it is not present
r+-> read and write
w+-> write and read
a+-> write and read
wb,rb for binary number files
'''
#giving r before path makes python think it is a raw data so that it doesn't look for in-built functonalities
#\\ is because that some folders have password or encrypted protectioon so that python is unable to create it thus \\ makes it created
#otherwise just give a single \
a.write('Heat wave Holidays\n')
a.write('But online classes\n')
l=['Hi',', Good',' Morning']
for i in l:
    a.write(i)
a.write('\n')
a.writelines(l)#written in a single line
a.close()
'''
2nd method for creating or adding a list info the file
with open(r'E:\\T-Hub\\2nd Semester\\Python Programming\\example.txt','w') as f:
    f.writelines(l)
    f.close()
'''
#if file is not there and you try to read it, python shell shows FileNotFoundError
a=open(r'E:\\T-Hub\\2nd Semester\\Python Programming\\example.txt','r')
#b=a.read()
b=a.readlines()#makes a list and prints line by line
for i in b:
    print(i)
a.close()
a=open(r'E:\\T-Hub\\2nd Semester\\Python Programming\\example.csv','w')
#.xlsx shows error when opening but creating a csv file (same as excel) doesn't shows any error
a.write('Heat wave Holidays\n')
a.write('But online classes\n')
a.close()
a=open(r'E:\\T-Hub\\2nd Semester\\Python Programming\\example.csv','r')
b=a.readlines()
for i in b:
    print(i)
a.close()
a=open(r'E:\T-Hub\2nd Semester\Python Programming\cars.csv','r')
b=a.readlines()
c=[]
for i in b:
    i=i.split(',')
    c.append(i)
print(c)
a.close()
