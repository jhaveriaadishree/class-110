import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
df= pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("population_mean-",population_mean)
print("std_deviation-",std_deviation)
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()