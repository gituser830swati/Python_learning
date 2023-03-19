
# with user

n= int(input("Enter first num:"))
s= int(input("Enter second num:"))
for i in range(n,s):
   for j in range(n,i+1):
      print(chr(j),end='')
   print()

