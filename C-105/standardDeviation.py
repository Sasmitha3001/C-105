import csv
import math

f=open('data.csv')
read=csv.reader(f)
read=list(read)

#print(read)
data=read[0]
#print(data)

length=len(data)
sum=0

for i in data:
    sum=sum+int(data[i])

mean=sum/length
print(str(mean))

squaredList=[]

for number in data:
    a=int(number)-mean(data)
    a=a*a
    squaredList.append(a)

total=0
for i in squaredList:
    total=total+i

result=total/(length-1)
standardDeviation=math.sqrt(result)

print("The standard Deviation is:"+str(standardDeviation))

