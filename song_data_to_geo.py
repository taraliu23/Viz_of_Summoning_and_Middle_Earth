import pandas as pd
import geopandas as gpd
import seaborn
import folium

db = gpd.read_file("/Users/rainylty/STUDY/IVth/datascience/summer_school/summoning_and_lotr/Viz_of_Summoning_and_Middle_Earth/final_geo_data/with_coords.shp")

# db.info

# seaborn.jointplot(x='xcoord',y='ycoord', data=db, s=0.5)

# map = db.explore()

my_map = folium.Map(
    # location=[],
    zoom_start=2,
    
)

my_map

poi = pd.read_csv('final_geo_data/location_of_poi2.csv')
poi.head(3)

# x = pd.to_numeric(poi['xcoord'], errors='coerce')
# y = pd.to_numeric(poi['ycoord'], errors='coerce')


city = poi.loc[0]
folium.Marker(
    location=[39.916668,116.383331]
).add_to(my_map)

my_map