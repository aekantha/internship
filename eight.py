# 8.  TAKE A NUMERIC VALUE FROM USER. PRINT THE SUM THE DIGITS OF THAT NUMBER.
value=input('enter the numeric value :')
sum=0
for i in value:
    sum=sum+int(i)
print("The sum of the digit of this number is",sum)

