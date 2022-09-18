import pandas as pd
import geopandas as gpd
import seaborn

db = gpd.read_file("/Users/rainylty/STUDY/IVth/datascience/summer_school/summoning_and_lotr/Viz_of_Summoning_and_Middle_Earth/final_geo_data/with_coords.shp")

db.info

seaborn.jointplot(x='xcoord',y='ycoord', data=db, s=0.5)