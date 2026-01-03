import geopandas as gpd
import os

# Lataa taso
path = "/mnt/c/Users/Käyttäjä/Documents/jarvet_drop_gpkg.gpkg"
gdf = gpd.read_file(path, layer="jarvet_drop_gpkg")

# Erottele MultiPolygonit yksittäisiksi Polygon-featuureiksi
gdf_exploded = gdf.explode(index_parts=False)

# Hae nykyinen työskentelykansio (scriptin kansio)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Luo output-polku samaan kansioon
output_path = os.path.join(current_dir, "jarvet_polygon.gpkg")

# Tallenna output
gdf_exploded.to_file(output_path, driver="GPKG")

# Tulosta Polygonien määrä ja output path
print("Done. Output saved in:", output_path)
print("Number of Polygon features in output:", len(gdf_exploded))