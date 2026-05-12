"""
Sentinel-2 GeoMAD annual product configuration
"""
from ...common.resource_limits import GEOMAD_S2_LIMIT
from ..bands.s2_geomad import S2_GEOMAD_BANDS_INFO, S2_GEOMAD_BANDS
from ..styles.s2_geomad import (
    S2_GEOMAD_RGB,
    S2_GEOMAD_FALSE_COLOR,
    S2_GEOMAD_REDEDGE,
    S2_GEOMAD_NDVI,
    S2_GEOMAD_NDVI_RE,
    S2_GEOMAD_NDWI,
    S2_GEOMAD_MNDWI,
    S2_GEOMAD_NDBI,
    S2_GEOMAD_NDMI,
    S2_GEOMAD_BSI,
    S2_GEOMAD_EMAD,
    S2_GEOMAD_SMAD,
    S2_GEOMAD_BCMAD,
    S2_GEOMAD_TERNARY_MAD,
    S2_GEOMAD_COUNT,
)

s2_geomad_annual_layer = {
    "title": "Annual GeoMAD (Sentinel-2)",
    "name": "s2_geomad_annual",
    "abstract": """
                GeoMAD (Geometric Median Absolute Deviation) statistics over Indonesia
                """,
    "product_name": "s2_geomad_annual",

    "resource_limits": GEOMAD_S2_LIMIT,

    "bands": S2_GEOMAD_BANDS,
    "feature_info": {
        "include_utc_dates": True,
        "include_bands": S2_GEOMAD_BANDS_INFO,
    },

    "dynamic": False,
    "time_resolution": "summary",
    "default_time": "latest",

    "image_processing": {
        "extent_mask_func": ["ows_config.common.band_utils.mask_by_emad_nan"],
        "always_fetch_bands": ["EMAD"],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },

    "native_crs": "EPSG:6933",
    "native_resolution": [10, -10],

    "styling": {
        "default_style": "rgb",
        "styles": [
            S2_GEOMAD_RGB,
            S2_GEOMAD_FALSE_COLOR,
            S2_GEOMAD_REDEDGE,
            S2_GEOMAD_NDVI,
            S2_GEOMAD_NDVI_RE,
            S2_GEOMAD_NDWI,
            S2_GEOMAD_MNDWI,
            S2_GEOMAD_NDBI,
            S2_GEOMAD_NDMI,
            S2_GEOMAD_BSI,
            S2_GEOMAD_EMAD,
            S2_GEOMAD_SMAD,
            S2_GEOMAD_BCMAD,
            S2_GEOMAD_TERNARY_MAD,
            S2_GEOMAD_COUNT,
        ],
    },
}
