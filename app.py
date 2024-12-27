import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Load GeoJSON data
geojson_path = "SVI_NDVI_Export.geojson"  # Path to your GeoJSON file
with open(geojson_path, "r") as file:
    geojson_data = json.load(file)

# Streamlit title and description
st.title("Interactive Map for Drought Monitoring")
st.write("This map visualizes the SVI and NDVI data in an interactive format.")

# Create the base map using Folium
m = folium.Map(location=[37.7795, 122.4203], zoom_start=10)  # Adjust the coordinates for your area

# Add the GeoJSON data to the map
folium.GeoJson(geojson_data).add_to(m)

# Display the map in the Streamlit app
st_folium(m, width=700, height=500)

