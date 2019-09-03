import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import folium

df_can = pd.read_excel('.\\immigration-to-canada-ibm-dataset\\Canada.xlsx',
                       sheet_name="Canada by Citizenship",
                       skiprows=list(range(20)),
                       skipfooter=2)

# clean up the dataset to remove unnecessary columns (eg. REG)
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# let's rename the columns so that they make sense
df_can.rename(columns={
    'OdName': 'Country',
    'AreaName': 'Continent',
    'RegName': 'Region'
},
              inplace=True)

# for sake of consistency, let's also make all column labels of type string
df_can.columns = list(map(str, df_can.columns))

# add total column
df_can['Total'] = df_can.sum(axis=1)

world_geo = r'world_countries.json'
# create a numpy array of length 6 and has linear spacing from the minium total
#  immigration to the maximum total immigration
threshold_scale = np.linspace(df_can['Total'].min(),
                              df_can['Total'].max(),
                              6,
                              dtype=int)
threshold_scale = threshold_scale.tolist()  # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1
# make sure that the last value of the list is greater than the maximum immigration

zoom = 2.5
world_map = folium.Map(location=[1, 1],
                       zoom_start=zoom,
                       min_zoom=zoom,
                       max_zoom=zoom,
                       zoom_control=False,
                       no_touch=True)

# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
folium.Choropleth(geo_data=world_geo,
                  data=df_can,
                  columns=['Country', 'Total'],
                  key_on='feature.properties.name',
                  threshold_scale=threshold_scale,
                  nan_fill_color='purple',
                  nan_fill_opacity=0.4,
                  fill_color='YlGn',
                  line_color='blue',
                  line_weight=2,
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name='Immigration to Canada').add_to(world_map)

world_map.save('world_map.html')
