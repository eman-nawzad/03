import streamlit as st
import folium
from streamlit_folium import st_folium

# Minimal GeoJSON
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "Test Region", "SPI": -1.5, "NDVI": 0.6},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [42.85, 35.5],
                        [42.87, 35.5],
                        [42.87, 35.52],
                        [42.85, 35.52],
                        [42.85, 35.5]
                    ]
                ],
            },
        }
    ],
}

# Create a Folium map
m = folium.Map(location=[35.5, 42.85], zoom_start=8)
folium.GeoJson(geojson_data, name="Test Data").add_to(m)

# Display the map in Streamlit
st.title("Minimal Drought Monitoring App")
st_folium(m, width=700, height=500)

