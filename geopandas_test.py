# Import necessary libraries
import geopandas as gpd

# Load a GeoJSON file containing geospatial data
url = "https://raw.githubusercontent.com/nmota/caop_GeoJSON/master/ContinenteConcelhos.geojson"
districts = gpd.read_file(url)

# Plot the geospatial data
districts.plot()
