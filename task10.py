n=int(input("Numbers between 100 and 200, divisible by 9:"))
k=0
l=0
m=0
h=0

while l<=n:
     while k>=0:
          if k%m!=0:
               h+=1
               print(k)
               m+=1
               k+=1
          if h==0:
            l+=1
          