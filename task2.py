a=int(input())
n=0
for i in range(1,a+1):
  if a%i==0 :
    n+=1
    if n<=2:
     print("The entered number is a prime number.")
    elif n>2 : print("The entered number is a not prime number.")