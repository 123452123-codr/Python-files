n = int(input("Enter the number for which the facotrial is required:"))
ft = 1
i = 1

while i <= n:
    ft *= i
    i += 1
print("{}! = {}".format(n,ft))
