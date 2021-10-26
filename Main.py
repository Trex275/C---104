import csv
from collections import Counter

with open("C104/archive/SOCR-HeightWeight.csv")as file: 
    reader = csv.reader(file)
    data = list(reader)

data.pop(0)
height = []
for i in range(len(data)): 
    newdata = data[i][1]
    height.append(newdata)
n = len(height)
sum = 0
for h in height: 
    sum = sum + float (h)
mean = sum/n
print(mean)
#Median

height.sort()
if n%2 == 0:
    median1 = float(height[n//2])
    median2 = float(height[n//2 -1])
    median = (median1 + median2)/2
    print(median)
else: 
    median = float(height[n//2])
    print(median)
#Mode

counter1 = Counter(height)
print(counter1)