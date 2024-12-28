import json
import folium
import streamlit as st
from streamlit_folium import st_folium

# Title
st.title("Drought Monitoring Application")

# Load GeoJSON data
geojson_path = "SVI_NDVI_Export.geojson"
with open(geojson_path, "r") as f:
    data = json.load(f)

# Create a Folium map
m = folium.Map(location=[35.5, 42.85], zoom_start=8)
folium.GeoJson(data, name="Drought Data").add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)

# Display information about the data
st.sidebar.title("Drought Data Details")
for feature in data["features"]:
    properties = feature["properties"]
    st.sidebar.write(f"Region: {properties.get('name', 'N/A')}")
    st.sidebar.write(f"SPI: {properties.get('SPI', 'N/A')}")
    st.sidebar.write(f"NDVI: {properties.get('NDVI', 'N/A')}")
    st.sidebar.write("---")

