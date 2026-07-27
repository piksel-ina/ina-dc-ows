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

_GEOMAD_COMMON = {
    "abstract": """
                GeoMAD (Geometric Median and Median Absolute Deviation) annual composite
                over Indonesia, derived from Sentinel-2 surface reflectance.
                """,
    "product_name": "s2_geomad_annual",
    "resource_limits": GEOMAD_S2_LIMIT,
    "bands": S2_GEOMAD_BANDS,
    "feature_info": {
        "include_utc_dates": True,
        "include_bands": S2_GEOMAD_BANDS_INFO,
    },
    "dynamic": False,
    "time_resolution": "year", # TODO: Update "The 'year' time resolution type is deprecated.  Please use 'summary'."
    "default_time": "latest",
    "native_crs": "EPSG:6933",
    "native_resolution": [10, -10],
    "low_res_product_name": "s2_geomad_annual_120",
}

_GEOMAD_SPECTRAL_BASE = {
    **_GEOMAD_COMMON,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
}

_GEOMAD_BASE = {
    **_GEOMAD_COMMON,
    "image_processing": {
        "extent_mask_func": ["ows_config.common.band_utils.mask_by_emad_nan"],
        "always_fetch_bands": ["EMAD"],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
}

s2_geomad_annual_spectral_layer = {
    **_GEOMAD_SPECTRAL_BASE,
    "title": "GeoMAD Annual - Spectral (Sentinel-2)",
    "name": "s2_geomad_annual_spectral",
    "styling": {
        "default_style": "rgb",
        "styles": [
            S2_GEOMAD_RGB,
            S2_GEOMAD_FALSE_COLOR,
            S2_GEOMAD_REDEDGE,
        ],
    },
}

s2_geomad_annual_indices_layer = {
    **_GEOMAD_SPECTRAL_BASE,
    "title": "GeoMAD Annual - Spectral Indices (Sentinel-2)",
    "name": "s2_geomad_annual_indices",
    "styling": {
        "default_style": "ndvi",
        "styles": [
            S2_GEOMAD_NDVI,
            S2_GEOMAD_NDVI_RE,
            S2_GEOMAD_NDWI,
            S2_GEOMAD_MNDWI,
            S2_GEOMAD_NDBI,
            S2_GEOMAD_NDMI,
            S2_GEOMAD_BSI,
        ],
    },
}

s2_geomad_annual_statistics_layer = {
    **_GEOMAD_BASE,
    "title": "GeoMAD Annual - Statistics (Sentinel-2)",
    "name": "s2_geomad_annual_statistics",
    "styling": {
        "default_style": "log_emad",
        "styles": [
            S2_GEOMAD_EMAD,
            S2_GEOMAD_SMAD,
            S2_GEOMAD_BCMAD,
            S2_GEOMAD_TERNARY_MAD,
            S2_GEOMAD_COUNT,
        ],
    },
}
