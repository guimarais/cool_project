# Import necessary libraries
import geopandas as gpd
import matplotlib.pyplot as plt

# Load a GeoJSON file containing geospatial data
url = "https://raw.githubusercontent.com/nmota/caop_GeoJSON/master/ContinenteConcelhos.geojson"
portugal = gpd.read_file(url)

fig, ax = plt.subplots(figsize=(10, 10))

# Plot the geospatial data
portugal.plot(ax=ax, color='lightblue', edgecolor='black')
