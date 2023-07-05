# 2.  TAKE THREE NUMBERS FROM USER AS INPUTS. PRINT THE SMALLEST NUMBER BETWEEN THOSE NUMBERS BY USING IF-ELSE STATEMENTS.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Smallest number determination
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Output the smallest number
print("The smallest number is:",smallest)