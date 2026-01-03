import geopandas as gpd

path = "/mnt/c/Users/Käyttäjä/Documents/jarvet_drop_gpkg.gpkg"

gdf = gpd.read_file(path)

print(gdf.geometry.type.value_counts())