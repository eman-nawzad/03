# Interactive Map for Drought Monitoring

This repository contains a Streamlit web application that displays an interactive map with SVI and NDVI data visualized through a GeoJSON layer.

## Requirements

- streamlit
- folium
- streamlit-folium

You can install the dependencies using:

```bash
pip install -r requirements.txt
streamlit run app.py


### 4. **`SVI_NDVI_Export.geojson`**

Ensure your GeoJSON file (located as `SVI_NDVI_Export.geojson`) is correctly structured and placed in the project directory. This file will be used to visualize the data on the map.

### Running the App

After setting up these files, you can run the Streamlit app using the following command:

```bash
streamlit run app.py
