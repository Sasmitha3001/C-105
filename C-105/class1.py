import csv

f=open('class1.csv')
read=csv.reader(f)
data=list(read)
data.pop(0)

length=len(data)
sum=0

for data in data:
    sum=sum+int(data[1])

mean=sum/length
print("The mean is: "+str(mean))

import pandas as p
import plotly.express as px

panda=p.read_csv('class1.csv')
graph=px.scatter(panda,x='Student Number',y='Marks',title="Student Marks")
graph.update_layout(shapes=[
    dict(
        type='line',
        x0=0,
        x1=length,
        y0=mean,
        y1=mean
    )
])


graph.show()