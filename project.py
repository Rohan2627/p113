import pandas as pd
import plotly.express as px

import numpy as np

data  = pd.read_csv("heightWeight.csv")

height = data["Height"].tolist()
weight = data["Weight"].tolist()

fig = px.scatter(data, x = height  ,  y = weight )
fig.show()