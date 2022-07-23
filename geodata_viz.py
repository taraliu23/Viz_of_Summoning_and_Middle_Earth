import geopandas as gpd
df = gpd.read_file('geo_data/new_layers/realms.shp')
df.head()

df.explore()