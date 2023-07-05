# 5.  MAKE A PARAMETERIZED FUNCTION, WHICH WILL TAKE SOMEONE'S AGE AS USER INPUT AND WILL PRINT THE VALUE DOUBLE OF THEIR AGE, WHEN THE FUNCTION IS CALLED.
def double_age():
    age = int(input("Enter your age: "))
    double = age * 2
    print("Double of your age is:", double)

double_age()