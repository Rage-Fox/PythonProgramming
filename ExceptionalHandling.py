#exceptional handling doesn't stop the program even if it as any error
try:
    a=10
    print(a+b)
    print(a/0)
except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Zero Division Error")
else:#executes when try block has no error
    print("No Error")
finally:
    print("Done!")
a=float(input())
if(a>=0 and a<=10):
    print("My CGPA is:",a)
else:
    raise Exception("Enter Valid Details")
