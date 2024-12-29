import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load GeoJSON data
@st.cache_data
def load_data():
    return gpd.read_file("SVI_NDVI_Export.geojson")

# Add SPI thresholds legend
def add_drought_legend(map_object):
    legend_html = """
    <div style='position: fixed; 
                bottom: 50px; left: 50px; width: 250px; height: 180px; 
                background-color: white; z-index:9999; font-size:14px;
                border: 2px solid black; padding: 10px'>
        <b>Drought Categories (SPI):</b><br>
        <i style="background: #ff0000; width: 20px; height: 10px; display: inline-block;"></i> Extreme Drought (< -2.00)<br>
        <i style="background: #ffa500; width: 20px; height: 10px; display: inline-block;"></i> Severe Drought (-1.50 to -1.99)<br>
        <i style="background: #ffff00; width: 20px; height: 10px; display: inline-block;"></i> Moderate Drought (-1.00 to -1.49)<br>
        <i style="background: #00ff00; width: 20px; height: 10px; display: inline-block;"></i> Mild Drought (-0.99 to -0.00)<br>
    </div>
    """
    map_object.get_root().html.add_child(folium.Element(legend_html))

# Add NDVI suitability legend
def add_ndvi_legend(map_object):
    legend_html = """
    <div style='position: fixed; 
                bottom: 50px; right: 50px; width: 250px; height: 100px; 
                background-color: white; z-index:9999; font-size:14px;
                border: 2px solid black; padding: 10px'>
        <b>Crop Suitability (NDVI):</b><br>
        <i style="background: #008000; width: 20px; height: 10px; display: inline-block;"></i> Suitable (0.36 - 0.65)<br>
        <i style="background: #d3d3d3; width: 20px; height: 10px; display: inline-block;"></i> Unsuitable<br>
    </div>
    """
    map_object.get_root().html.add_child(folium.Element(legend_html))

# Map SPI thresholds to colors
def classify_drought(spi):
    if spi < -2.00:
        return "#ff0000"  # Extreme drought
    elif -1.50 <= spi <= -1.99:
        return "#ffa500"  # Severe drought
    elif -1.00 <= spi <= -1.49:
        return "#ffff00"  # Moderate drought
    elif -0.99 <= spi <= -0.00:
        return "#00ff00"  # Mild drought
    else:
        return "#d3d3d3"  # No data

# Map NDVI values to suitability
def classify_ndvi(ndvi):
    if 0.36 <= ndvi <= 0.65:
        return "#008000"  # Suitable for crops
    else:
        return "#d3d3d3"  # Unsuitable for crops

# Main application
st.title("Drought and Crop Suitability Monitoring")
st.sidebar.header("Options")
show_drought = st.sidebar.checkbox("Show Drought Data (SPI)", value=True)
show_ndvi = st.sidebar.checkbox("Show Crop Suitability (NDVI)", value=True)

# Load data
data = load_data()

# Create map
m = folium.Map(location=[data.geometry.centroid.y.mean(), data.geometry.centroid.x.mean()], zoom_start=8)

# Add SPI drought data
if show_drought:
    for _, row in data.iterrows():
        color = classify_drought(row["SPI"])
        folium.GeoJson(
            row.geometry,
            style_function=lambda feature, color=color: {
                "fillColor": color,
                "color": "black",
                "weight": 0.5,
                "fillOpacity": 0.7
            }
        ).add_to(m)
    add_drought_legend(m)

# Add NDVI suitability data
if show_ndvi:
    for _, row in data.iterrows():
        color = classify_ndvi(row["NDVI"])
        folium.GeoJson(
            row.geometry,
            style_function=lambda feature, color=color: {
                "fillColor": color,
                "color": "black",
                "weight": 0.5,
                "fillOpacity": 0.7
            }
        ).add_to(m)
    add_ndvi_legend(m)

# Render map
st_folium(m, width=700, height=500)

