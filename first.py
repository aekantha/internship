
# 1.  TAKE A WORD AS INPUT FROM USER. PRINT THE TOTAL NUMBER OF VOWELS IN THE WORD.
word=input("enter the word:")
vowels="aeiou"
count=0
for i in word:
    if i in vowels:
        count=count+1
print("Total no. of vowels in the word are:  ",count)


