#Python program to check whether a given number is palindrome Number or not.

i = int(input("Enter Number:"))
rev = 0
x = i
while(i>0):
   rev=(rev*10)+i%10
   i=i//10
if(x==rev):
   print("Palindrome Number")
else:
   print("Palindrome Number")
