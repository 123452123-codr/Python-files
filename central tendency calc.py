import statistics as s

a = int(input("Enter number of elements : "))

data = list(map(int,input("\nEnter the numbers : ").strip().split()))[:a]

mean = s.mean(data)
mode = s.mode(data)
median = s.median(data)

print("Mean = {}\nMedian = {}\nMode = {}".format(mean,int(median),mode))