"""
Spectral index styles for Landsat Collection 2 Level-2 Surface Reflectance
"""

NDVI = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index, indeks yang menggambarkan keberadaan dan kerapatan vegetasi",
    "index_expression": "(nir*1.0-red)/(nir+red-14545.4545)",
    "color_ramp": [
        {"value": -0.0, "color": "#8F3F20", "alpha": 0.0},
        {"value": 0.0, "color": "#8F3F20", "alpha": 1.0},
        {"value": 0.1, "color": "#A35F18"},
        {"value": 0.2, "color": "#B88512"},
        {"value": 0.3, "color": "#CEAC0E"},
        {"value": 0.4, "color": "#E5D609"},
        {"value": 0.5, "color": "#FFFF0C"},
        {"value": 0.6, "color": "#C3DE09"},
        {"value": 0.7, "color": "#88B808"},
        {"value": 0.8, "color": "#529400"},
        {"value": 0.9, "color": "#237100"},
        {"value": 1.0, "color": "#114D04"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 1.0,
        "ticks": [0.0, 0.5, 1.0],
    }
}

NDWI = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index, indeks yang menggambarkan keberadaan air",
    "index_expression": "(green*1.0-nir)/(green+nir-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.1, "color": "#b0d2e8"},
        {"value": 0.2, "color": "#73b3d8"},
        {"value": 0.3, "color": "#3e8ec4"},
        {"value": 0.4, "color": "#1563aa"},
        {"value": 0.5, "color": "#08306b"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 0.5,
        "ticks": [0.0, 0.25, 0.5]
    }
}

MNDWI = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index, indeks yang menggambarkan keberadaan air (Xu 2006)",
    "index_expression": "(green*1.0-swir_1)/(green+swir_1-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 1.0,
        "ticks": [0.0, 0.5, 1.0]
    }
}

NDBI = {
    "name": "ndbi",
    "title": "NDBI - SWIR, NIR",
    "abstract": "Normalised Difference Built-up Index, indeks yang menggambarkan keberadaan kawasan terbangun",
    "index_expression": "(swir_1*1.0-nir)/(swir_1+nir-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#feebe2"},
        {"value": 0.2, "color": "#fa9fb5"},
        {"value": 0.4, "color": "#f768a1"},
        {"value": 0.6, "color": "#dd3497"},
        {"value": 0.8, "color": "#ae017e"},
        {"value": 1.0, "color": "#7a0177"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 1.0,
        "ticks": [0.0, 0.5, 1.0],
    }
}

NDMI = {
    "name": "ndmi",
    "title": "NDMI - NIR, SWIR",
    "abstract": "Normalised Difference Moisture Index, indeks yang menggambarkan kandungan air pada daun",
    "index_expression": "(nir*1.0-swir_1)/(nir+swir_1-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.1, "color": "#b0d2e8"},
        {"value": 0.2, "color": "#73b3d8"},
        {"value": 0.3, "color": "#3e8ec4"},
        {"value": 0.4, "color": "#1563aa"},
        {"value": 0.5, "color": "#08306b"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 0.5,
        "ticks": [0.0, 0.25, 0.5]
    }
}

LANDSAT_INDEX_STYLES = [
    NDVI,
    NDWI,
    MNDWI,
    NDBI,
    NDMI,
]
