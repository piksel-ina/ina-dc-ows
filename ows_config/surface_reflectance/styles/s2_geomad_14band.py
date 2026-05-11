"""
Styles for Sentinel-2 GeoMAD 14-band annual product
"""

S2_GEOMAD_14_RGB = {
    "name": "rgb",
    "title": "Geomedian - Red, Green, Blue",
    "abstract": "True-colour image, using the red, green and blue bands",
    "components": {
        "red": {"red": 1.0},
        "green": {"green": 1.0},
        "blue": {"blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "multi_date": [
        {
            "allowed_count_range": [2, 4],
            "animate": True,
        }
    ],
}

S2_GEOMAD_14_FALSE_COLOR = {
    "name": "false_color_nir",
    "title": "False Colour - NIR, Red, Green",
    "abstract": "False-colour image using NIR, red and green bands for vegetation analysis",
    "components": {
        "red": {"nir": 1.0},
        "green": {"red": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "multi_date": [
        {
            "allowed_count_range": [2, 4],
            "animate": True,
        }
    ],
}

S2_GEOMAD_14_REDEDGE = {
    "name": "false_color_rededge",
    "title": "False Colour - Red Edge, NIR, Red",
    "abstract": "False-colour composite using red edge 2, NIR and red bands",
    "components": {
        "red": {"rededge2": 1.0},
        "green": {"nir": 1.0},
        "blue": {"red": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "multi_date": [
        {
            "allowed_count_range": [2, 4],
            "animate": True,
        }
    ],
}

S2_GEOMAD_14_NDVI = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir", "band2": "red"},
    },
    "needed_bands": ["red", "nir"],
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
    },
}

S2_GEOMAD_14_NDVI_RE = {
    "name": "ndvi_rededge",
    "title": "NDVI - Red Edge 1, NIR",
    "abstract": "Red Edge NDVI using red edge 1 and NIR narrow bands",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir08", "band2": "rededge1"},
    },
    "needed_bands": ["rededge1", "nir08"],
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
    },
}

S2_GEOMAD_14_NDWI = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index for surface water detection",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "nir"},
    },
    "needed_bands": ["green", "nir"],
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
        "ticks": [0.0, 0.25, 0.5],
    },
}

S2_GEOMAD_14_MNDWI = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index for improved water detection in built-up areas",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "swir16"},
    },
    "needed_bands": ["green", "swir16"],
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
        "ticks": [0.0, 0.5, 1.0],
    },
}

S2_GEOMAD_14_NDBI = {
    "name": "ndbi",
    "title": "NDBI - SWIR, NIR",
    "abstract": "Normalised Difference Built-up Index for urban area detection",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "swir16", "band2": "nir"},
    },
    "needed_bands": ["nir", "swir16"],
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
    },
}

S2_GEOMAD_14_NDMI = {
    "name": "ndmi",
    "title": "NDMI - NIR, SWIR",
    "abstract": "Normalised Difference Moisture Index for vegetation water content",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir", "band2": "swir16"},
    },
    "needed_bands": ["nir", "swir16"],
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
        "ticks": [0.0, 0.25, 0.5],
    },
}

S2_GEOMAD_14_BSI = {
    "name": "bsi",
    "title": "BSI - Bare Soil Index",
    "abstract": "Bare Soil Index using SWIR, Red, NIR and Blue bands for soil exposure detection",
    "index_function": {
        "function": "ows_config.common.band_utils.bare_soil_index",
        "mapped_bands": True,
        "kwargs": {"swir": "swir16", "red": "red", "nir": "nir", "blue": "blue"},
    },
    "needed_bands": ["blue", "red", "nir", "swir16"],
    "color_ramp": [
        {"value": -0.2, "color": "#1a9850", "alpha": 0.0},
        {"value": 0.0, "color": "#91cf60"},
        {"value": 0.1, "color": "#d9ef8b"},
        {"value": 0.2, "color": "#fee08b"},
        {"value": 0.3, "color": "#fdae61"},
        {"value": 0.4, "color": "#f46d43"},
        {"value": 0.5, "color": "#d73027"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 0.5,
        "ticks": [0.0, 0.25, 0.5],
    },
}

S2_GEOMAD_14_EMAD = {
    "name": "emad",
    "title": "EMAD - Euclidean MAD",
    "abstract": "Euclidean Median Absolute Deviation - measures overall spectral change. Higher values indicate greater change from the geomedian.",
    "components": {
        "red": {"EMAD": 1.0},
        "green": {"EMAD": 1.0},
        "blue": {"EMAD": 1.0},
    },
    "scale_range": [0.0, 0.05],
    "legend": {
        "begin": 0.0,
        "end": 0.05,
        "ticks": [0.0, 0.025, 0.05],
    },
}

S2_GEOMAD_14_SMAD = {
    "name": "smad",
    "title": "SMAD - Spectral MAD",
    "abstract": "Spectral Median Absolute Deviation - measures spectral variability. Higher values indicate more spectral variation over the composite period.",
    "components": {
        "red": {"SMAD": 1.0},
        "green": {"SMAD": 1.0},
        "blue": {"SMAD": 1.0},
    },
    "scale_range": [0.0, 0.05],
    "legend": {
        "begin": 0.0,
        "end": 0.05,
        "ticks": [0.0, 0.025, 0.05],
    },
}

S2_GEOMAD_14_BCMAD = {
    "name": "bcmad",
    "title": "BCMAD - Bray-Curtis MAD",
    "abstract": "Bray-Curtis Median Absolute Deviation - measures compositional change. Higher values indicate greater spectral dissimilarity.",
    "components": {
        "red": {"BCMAD": 1.0},
        "green": {"BCMAD": 1.0},
        "blue": {"BCMAD": 1.0},
    },
    "scale_range": [0.0, 0.05],
    "legend": {
        "begin": 0.0,
        "end": 0.05,
        "ticks": [0.0, 0.025, 0.05],
    },
}

S2_GEOMAD_14_COUNT = {
    "name": "count",
    "title": "Observation Count",
    "abstract": "Number of clear observations used in the annual composite. Higher values indicate more cloud-free acquisitions.",
    "components": {
        "red": {"COUNT": 1.0},
        "green": {"COUNT": 1.0},
        "blue": {"COUNT": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "legend": {
        "begin": 0,
        "end": 100,
        "ticks": [0, 25, 50, 75, 100],
    },
}
