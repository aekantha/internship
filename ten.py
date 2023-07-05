# 10. TAKE TWO NUMERIC INTEGER VALUES FROM USER. PRINT THE DIFFERENCE OF THEIR VALUES IF THOSE TWO NUMBERS ARE SAME. PRINT THE HIGHER VALUE IF THOSE TWO NUMBERS ARE DIFFERENT.
a=int(input("enter the first int value :"))
b=int(input("enter the second int value : "))
if a==b:
    print("the difference of their value is",a-b)
else:
    print("the higher value is",max(a,b))