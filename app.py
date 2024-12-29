import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Function to load the GeoJSON file
def load_geojson(file_path):
    st.write(f"Loading GeoJSON from {file_path}")
    return gpd.read_file(file_path)

# Load SVI GeoJSON data
try:
    svi_geojson = load_geojson('SVI_NDVI_Export.geojson')
    st.write("GeoJSON loaded successfully")
except Exception as e:
    st.write(f"Error loading GeoJSON: {e}")

# Streamlit layout
st.title("Drought Monitoring with SVI Data")
st.write("This application displays drought monitoring data using the SVI data.")

# Create map with Folium
m = folium.Map(location=[33.6, 44.3], zoom_start=10)

# Add GeoJSON layer for SVI data
folium.GeoJson(svi_geojson).add_to(m)

# Render the map in Streamlit
st_folium(m, width=700, height=500)

# Display a summary of the data
st.subheader("SVI Data Summary")
st.write(svi_geojson.head())



