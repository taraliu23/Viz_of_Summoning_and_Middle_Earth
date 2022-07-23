import geopandas as gpd
import folium
from folium.plugins import HeatMap


df = gpd.read_file('geo_data/new_layers/realms.shp')
df.head()

# create an interactive map
df.explore()

# to draw: HeatMap