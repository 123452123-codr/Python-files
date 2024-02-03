n = int(input("Enter the number to be checked:"))
p = int(n/2)
prime = 1

for i in range(2,p+1,1):
    if(n % i == 0):
        prime = 0
        break
if(prime == 1):
    print(n," is a prime number")
else:
    print(n," is not a prime number")