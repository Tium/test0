import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium


df=pd.read_csv('Incidents2016_.csv',index_col=False)

df_dist=df['PdDistrict'].value_counts()

header=["Neighborhood","Count"]

df_dist=df_dist.reset_index()
df_dist.columns=header

geo=r'san-francisco.geojson'
longitude = -122.419416
latitude = 37.774929

map = folium.Map(location=[latitude, longitude], zoom_start=12)

folium.Choropleth(
    geo_data=geo,
    data=df_dist,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
).add_to(map)

folium.LayerControl().add_to(map)
map.save('crime_map.html')

