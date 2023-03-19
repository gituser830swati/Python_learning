#Python program to check whether a given number is Armstrong Number or not.
# 153
 # 1^3+ 5^3 + 3^3
#    153

i = int(input("Enter Number to check for Armstrong:"))
orig=i
sum=0
while(i>0):
   sum = sum+(i%10)*(i%10)*(i%10)
   i=i//10
if orig==sum:
   print("Number is Armstrong")
else:
   print("Number is not Armstrong")   