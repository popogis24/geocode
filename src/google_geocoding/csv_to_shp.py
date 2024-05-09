import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Leia o arquivo CSV
df = gpd.read_file('/Users/andersonstolfi/Documents/coding/google_geocoding/xlsx/output.csv')
print(df.head())
# Crie uma coluna geometry com os pontos

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]

# Crie um GeoDataFrame
crs = {'init': 'epsg:4326'}  # WGS84
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

# Salve como shapefile
gdf.to_file('/Users/andersonstolfi/Documents/coding/google_geocoding/shapefile/pontos.shp')
