import pandas as pd
import plotly.express as px

import numpy as np

data  = pd.read_csv("heightWeight.csv")

height = data["Height"].tolist()
weight = data["Weight"].tolist()

# fig = px.scatter(data, x = height  ,  y = weight )
# fig.show()

# ------------------------------ equation of line ----------------

# y = mx + c

# -------------------------- Asumming m=1 , c=0  Using Hit & Trial Method --------------------------

m=1
c = 0
y = []

for x in height:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(data, x = height  ,  y = weight )
fig.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(height) , x1 = max(height),
        y0 = min(y) , y1=max(y)
    )
])
# fig.show()


# -------------------------- Asumming m=0.95 , c=93  Using Hit & Trial Method --------------------------

m= 0.95
c = -93
y = []

for x in height:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(data, x = height  ,  y = weight )
fig.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(height) , x1 = max(height),
        y0 = min(y) , y1=max(y)
    )
])
# fig.show()


x = 172
y = m * x + c
print(f"Weight of someone with height {x} is {y}")

# --------------------------------------------- Using Algorithm -------------------------------------------

heightArray = np.array(height)
weightArray = np.array(weight)

m,c = np.polyfit(heightArray , weightArray , 1)

print("--------------")
print(m,c)

y = []

for x in heightArray:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(data, x = heightArray  ,  y = weightArray )
fig.update_layout(shapes = [
    dict(
        type = 'line',
        x0 = min(heightArray) , x1 = max(heightArray),
        y0 = min(y) , y1=max(y)
    )
])
# fig.show()

# polynomial degree

# linear eq --> y = mx + c --> degree = 1
# 3x^2 + 5x -> degree = 2
