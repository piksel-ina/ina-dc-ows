from ...common.resource_limits import GEOMAD_S2_LIMIT
from ..bands.geomad_s2 import GEOMAD_S2_BANDS_INFO, GEOMAD_S2_BANDS
from ..styles.geomad_s2 import GEOMAD_S2_RGB

geomad_s2_annual_legacy_layer = {
    "title": "GeoMAD Annual - Legacy RGB (Sentinel-2)",
    "name": "geomad_s2_annual_legacy",
    "abstract": """
                Legacy 6-band GeoMAD (Geometric Median and Median Absolute Deviation)
                annual composite over Indonesia, derived from Sentinel-2 surface reflectance.
                Provided for quick visual comparison only.
                """,
    "product_name": "geomad_s2_annual",
    "resource_limits": GEOMAD_S2_LIMIT,
    "bands": GEOMAD_S2_BANDS,
    "feature_info": {
        "include_utc_dates": True,
        "include_bands": GEOMAD_S2_BANDS_INFO,
    },
    "dynamic": False,
    "time_resolution": "summary",
    "default_time": "latest",
    "native_crs": "EPSG:6933",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
    "styling": {
        "default_style": "rgb",
        "styles": [GEOMAD_S2_RGB],
    },
}
