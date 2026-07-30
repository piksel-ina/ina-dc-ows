"""
Pixel quality styles for Landsat Collection 2 Level-2 Surface Reflectance
"""

_NODATA_RULE = {
    "title": "",
    "abstract": "",
    "flags": {"nodata": True},
    "alpha": 0.0,
    "color": "#707070",
}

_CLOUD_RULE = {
    "title": "Awan",
    "abstract": "",
    "flags": {"cloud": "high_confidence"},
    "color": "#c2c1c0",
}

_DILATED_CLOUD_RULE = {
    "title": "Tepi Awan",
    "abstract": "",
    "flags": {"dilated_cloud": "dilated"},
    "color": "#b0afae",
}

_CIRRUS_RULE = {
    "title": "Awan Cirrus",
    "abstract": "",
    "flags": {"cirrus": "high_confidence"},
    "color": "#708090",
}

_CLOUD_SHADOW_RULE = {
    "title": "Bayangan Awan",
    "abstract": "",
    "flags": {"cloud_shadow": "high_confidence"},
    "color": "#4b4b37",
}

_SNOW_RULE = {
    "title": "Salju",
    "abstract": "",
    "flags": {"snow": "high_confidence"},
    "color": "Beige",
}

_WATER_RULE = {
    "title": "Air",
    "abstract": "",
    "flags": {"water": "water"},
    "color": "#4F81BD",
}

_LAND_RULE = {
    "title": "Darat",
    "abstract": "",
    "flags": {"water": "land_or_cloud"},
    "color": "#96966e",
}

LANDSAT_TM_PQ_STYLE = {
    "name": "pixel_quality",
    "title": "Kualitas Piksel",
    "abstract": "Klasifikasi kualitas piksel dari band qa_pixel: awan, tepi awan, bayangan awan, salju, air, dan darat",
    "value_map": {
        "pq": [
            _NODATA_RULE,
            _CLOUD_RULE,
            _DILATED_CLOUD_RULE,
            _CLOUD_SHADOW_RULE,
            _SNOW_RULE,
            _WATER_RULE,
            _LAND_RULE,
        ]
    },
}

LANDSAT_OLI_PQ_STYLE = {
    "name": "pixel_quality",
    "title": "Kualitas Piksel",
    "abstract": "Klasifikasi kualitas piksel dari band qa_pixel: awan, tepi awan, awan cirrus, bayangan awan, salju, air, dan darat",
    "value_map": {
        "pq": [
            _NODATA_RULE,
            _CLOUD_RULE,
            _DILATED_CLOUD_RULE,
            _CIRRUS_RULE,
            _CLOUD_SHADOW_RULE,
            _SNOW_RULE,
            _WATER_RULE,
            _LAND_RULE,
        ]
    },
}
