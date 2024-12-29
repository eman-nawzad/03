# Drought and Crop Suitability Monitoring Web Application

This web application visualizes drought conditions based on SPI (Standardized Precipitation Index) and assesses crop suitability using NDVI (Normalized Difference Vegetation Index) data. 

## Features
- Visualize drought levels using SPI data.
- Highlight crop suitability zones using NDVI values (0.36-0.65).
- Interactive map for exploring drought and crop suitability conditions.

## Drought Categorization (SPI)
The Standardized Precipitation Index (SPI) is used to classify drought conditions:
- **Extreme Drought:** Less than -2.00
- **Severe Drought:** -1.50 to -1.99
- **Moderate Drought:** -1.00 to -1.49
- **Mild Drought:** -0.99 to -0.00

## Crop Suitability (NDVI)
The NDVI values are used to assess crop suitability:
- **Suitable for Crops:** NDVI values between 0.36 and 0.65.
- **Unsuitable for Crops:** NDVI values outside this range.

## Repository Structure
- `app.py`: Streamlit application script that loads, processes, and displays the data on an interactive map.
- `SPI_12_GeoJSON.geojson`: GeoJSON data file containing SPI data for the region of interest.
- `SVI_NDVI_Export.geojson`: GeoJSON data file containing NDVI values for the region of interest.
- `requierment.txt`: A text file with the list of Python dependencies for running the app.

## Installation and Usage
To run this application on your local machine, follow these steps:

### 1. Clone this repository:
```bash
git clone https://github.com/eman-nawzad/03.git


