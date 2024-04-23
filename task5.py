def is_prime(n):
    counter = 0
    for i in range(1, n+1):
        if n%i==0:
            counter+=1
    if counter<=2: 
        return True
    else: 
        return False

n=int(input())
i=1
while i<=n:
    prime = is_prime(i)
    if prime==False:
        print(i, end=" ")
    i+=1
    


#     n=int(input())
# i=1
# while i<=n:
#     cnt=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             cnt+=1
#         j+=1
#     if cnt>2:
#         print(i,end=" ")
#     i+=1