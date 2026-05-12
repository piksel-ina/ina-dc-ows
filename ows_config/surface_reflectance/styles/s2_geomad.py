"""
Styles for Sentinel-2 GeoMAD annual product
"""

S2_GEOMAD_RGB = {
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

S2_GEOMAD_FALSE_COLOR = {
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

S2_GEOMAD_REDEDGE = {
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

S2_GEOMAD_NDVI = {
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

S2_GEOMAD_NDVI_RE = {
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

S2_GEOMAD_NDWI = {
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

S2_GEOMAD_MNDWI = {
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

S2_GEOMAD_NDBI = {
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

S2_GEOMAD_NDMI = {
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

S2_GEOMAD_BSI = {
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

_sdev_scaling = [0.020, 0.18]
_edev_scaling = [6.2, 7.3]
_bcdev_scaling = [0.025, 0.13]

S2_GEOMAD_EMAD = {
    "name": "log_emad",
    "title": "EMAD - Euclidean MAD (log)",
    "abstract": "Euclidean Median Absolute Deviation on a log scale. Measures overall spectral change; higher values indicate greater change from the geomedian.",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "EMAD",
            "scale_from": _edev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["EMAD"],
    "mpl_ramp": "magma",
    "range": [0.0, 4.0],
    "legend": {
        "begin": 0.0,
        "end": 4.0,
        "ticks": [0.0, 1.0, 2.0, 3.0, 4.0],
        "tick_labels": {
            "0.0": {"label": "Low"},
            "4.0": {"label": "High"},
        },
    },
}

S2_GEOMAD_SMAD = {
    "name": "arcsec_smad",
    "title": "SMAD - Spectral MAD (arcsec)",
    "abstract": "Spectral Median Absolute Deviation on an arcsec scale. Measures spectral variability; higher values indicate more spectral variation over the composite period.",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {
            "band": "SMAD",
            "scale_from": _sdev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["SMAD"],
    "mpl_ramp": "inferno",
    "range": [0.0, 4.0],
    "legend": {
        "begin": 0.0,
        "end": 4.0,
        "ticks": [0.0, 1.0, 2.0, 3.0, 4.0],
        "tick_labels": {
            "0.0": {"label": "Low"},
            "4.0": {"label": "High"},
        },
    },
}

S2_GEOMAD_BCMAD = {
    "name": "log_bcmad",
    "title": "BCMAD - Bray-Curtis MAD (log)",
    "abstract": "Bray-Curtis Median Absolute Deviation on a log scale. Measures compositional change; higher values indicate greater spectral dissimilarity.",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "BCMAD",
            "scale_from": _bcdev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["BCMAD"],
    "mpl_ramp": "cividis",
    "range": [0.0, 4.0],
    "legend": {
        "begin": 0.0,
        "end": 4.0,
        "ticks": [0.0, 1.0, 2.0, 3.0, 4.0],
        "tick_labels": {
            "0.0": {"label": "Low"},
            "4.0": {"label": "High"},
        },
    },
}

S2_GEOMAD_TERNARY_MAD = {
    "name": "tmad_rgb",
    "title": "MADs - SMAD, EMAD, BCMAD (RGB)",
    "abstract": "Ternary MAD composite: SMAD in red, EMAD in green, BCMAD in blue. Useful for visualising combined change patterns.",
    "components": {
        "red": {
            "function": "datacube_ows.band_utils.single_band_arcsec",
            "mapped_bands": True,
            "kwargs": {"band": "SMAD", "scale_from": _sdev_scaling},
        },
        "green": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {"band": "EMAD", "scale_from": _edev_scaling},
        },
        "blue": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {"band": "BCMAD", "scale_from": _bcdev_scaling},
        },
    },
    "additional_bands": ["SMAD", "EMAD", "BCMAD"],
}

S2_GEOMAD_COUNT = {
    "name": "count",
    "title": "Observation Count",
    "abstract": "Number of clear observations used in the annual composite. Higher values indicate more cloud-free acquisitions.",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "COUNT"},
    },
    "needed_bands": ["COUNT"],
    "mpl_ramp": "viridis",
    "range": [0.0, 120.0],
    "legend": {
        "begin": 0,
        "end": 120,
        "ticks": [0, 20, 40, 60, 80, 100, 120],
    },
}
