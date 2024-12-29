# Drought Monitoring Application with SVI Data

## Overview
This Streamlit application provides a visualization for drought monitoring using the **SVI (Social Vulnerability Index)** data. It leverages the **SVI NDVI** data to assess drought impacts and visualize them on a map. This application allows users to interactively explore the SVI data and monitor drought conditions in specific regions.

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/eman-nawzad/drought-monitoring.git
cd drought-monitoring


pip install -r requirements.txt
streamlit run app.py
Share


You said:
it is my repository structure in github :
README.md
SVI_NDVI_Export.geojson
app.py
requierment.txt                                                                                                                                                        give me script for every directory 
ChatGPT said:
ChatGPT
Here is a script suggestion for each file in your repository structure, ensuring functionality aligns with your drought monitoring app and thresholds.

1. README.md
This file will explain the purpose of the repository and how to use the application.

markdown
Copy code
# Drought Monitoring Web Application

This web application visualizes drought conditions based on SPI (Standardized Precipitation Index) and NDVI (Normalized Difference Vegetation Index) data. The app categorizes drought into various thresholds and displays them on an interactive map.

## Features
- Visualize drought levels using SPI data.
- Display NDVI data for vegetation analysis.
- Interactive map for exploring drought zones.

## Drought Categorization
- **Extreme Drought:** Less than -2.00
- **Severe Drought:** -1.50 to -1.99
- **Moderate Drought:** -1.00 to -1.49
- **Mild Drought:** -0.99 to -0.00

## Repository Structure
- `app.py`: Streamlit application script.
- `SVI_NDVI_Export.geojson`: GeoJSON data file for NDVI and SPI.
- `requierment.txt`: Python dependencies for running the app.

## Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
Install dependencies:
bash
Copy code
pip install -r requierment.txt
Run the app:
bash
Copy code
streamlit run app.py
Requirements
Python 3.8 or higher
Streamlit
GeoPandas
Matplotlib
Folium
License
This project is licensed under the MIT License.

css
Copy code

---

### 2. **`SVI_NDVI_Export.geojson`**
This is your GeoJSON file containing SPI and NDVI data. Ensure it includes SPI values so the app can use them for categorization.

No script is needed here, but ensure the data format is valid GeoJSON and includes necessary fields like `SPI` and `NDVI`.

---

### 3. **`app.py`**
This is the main Streamlit application script.

```python
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load GeoJSON data
@st.cache_data
def load_data():
    return gpd.read_file("SVI_NDVI_Export.geojson")

# Add SPI thresholds legend
def add_legend(map_object):
    legend_html = """
    <div style='position: fixed; 
                bottom: 50px; left: 50px; width: 250px; height: 180px; 
                background-color: white; z-index:9999; font-size:14px;
                border: 2px solid black; padding: 10px'>
        <b>Drought Categories:</b><br>
        <i style="background: #ff0000; width: 20px; height: 10px; display: inline-block;"></i> Extreme Drought (< -2.00)<br>
        <i style="background: #ffa500; width: 20px; height: 10px; display: inline-block;"></i> Severe Drought (-1.50 to -1.99)<br>
        <i style="background: #ffff00; width: 20px; height: 10px; display: inline-block;"></i> Moderate Drought (-1.00 to -1.49)<br>
        <i style="background: #00ff00; width: 20px; height: 10px; display: inline-block;"></i> Mild Drought (-0.99 to -0.00)<br>
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

# Main application
st.title("Drought Monitoring Web Application")
st.sidebar.header("Options")
show_ndvi = st.sidebar.checkbox("Show NDVI Data", value=True)

# Load data
data = load_data()

# Create map
m = folium.Map(location=[data.geometry.centroid.y.mean(), data.geometry.centroid.x.mean()], zoom_start=8)
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

# Add legend
add_legend(m)

# Render map
st_folium(m, width=700, height=500)
4. requierment.txt
This file will list all the dependencies needed for your application.

Copy code
streamlit
geopandas
folium
streamlit-folium
matplotlib
Let me know if you need further assistance!






