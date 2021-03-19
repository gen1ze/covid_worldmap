from scipy.interpolate import interp1d
from datetime import  date, timedelta
import pandas as pd
import plotly.express as px
import numpy as np
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

filename = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"

y = date.today() - timedelta(days = 1)
yesterday = y.strftime("X%m/%d/%y").replace('X0','X').replace('X','')
print(yesterday)

df = pd.read_csv(filename)
df.rename(columns = {'Country/Region': 'Country', yesterday : 'yesterday'},inplace = True)
df.drop("Province/State", axis = 1, inplace = True)

last_column = df[df.columns[-1]]
#print(last_column)
#print(df)

m = interp1d([1, max(last_column)],[5,40],fill_value="extrapolate")
circle_radius = m(last_column)
#df.head()

center = {'lat' :20.593684 , 'lon' :78.96288}
fig = px.density_mapbox(data_frame = df, lat = 'Lat', lon = 'Long', color_continuous_scale='thermal', radius = circle_radius, zoom = 0.6, mapbox_style = 'stamen-watercolor', hover_data = ['yesterday'] , hover_name = df.Country, title = 'total confirmed covid cases as of today', center = center)
fig.show(renderer="colab")
