#dictionaries are binding of key and value pairs together
#d={0:11,1:22,3:33,2:44}
#d={key:value}
#key can be an integer, float, string
#value can be string, int, float, bool, dictionary, list, set, tuple, etc....
#accessing only meant for a single key value
#modification is possible in dictionaries
d={'s1':[22,33,11],'s2':[44,33,21],'s3':[55,33,23]}
print(d['s1'])
print(len(d))
#important thngs for dictionaries
print(d.keys())
print(d.values())
print(d.items())
d['s2'].append('hello')
print(d)
d['s2'][0]=66#replacing 44 with 66 in 's2'
print(d)
d['s1']=88#converting list into integer for 's1'
print(d)
d['s4']=['new','value']#adding both new key and new value
print(d)
b={'s5':100,'s6':200}#adding two or more values to the existing dictionary
d.update(b)
print(d)
del d['s1']#deleting a particular key and it's value
print(d)
#there is no way to create a customised dictionary(scanning)
