#Python program to generate Fibonacci series until 'n' value
#  0 1 1 2 3 5 8 13 21.......
n = int(input("Enter Number: "))
x =0 
y = 1
z = 0
while(z<=n):
  print(z)
  x=y
  y=z
  z=x+y
