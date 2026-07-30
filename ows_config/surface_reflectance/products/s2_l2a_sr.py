"""
Sentinel-2 Surface Reflectance product configuration
"""

from ...common.resource_limits import SENTINEL2_LIMITS
from ..styles import S2_ALL_STYLES
from ..bands.sentinel2_bands import SENTINEL2_BANDS_INFO, SENTINEL2_BANDS

s2_l2a_layer = {
    "title": "Sentinel-2 L2A Surface Reflectance",
    "abstract": """
    Data Sentinel-2 L2A Surface Reflectance yang dibaca langsung dari arsip publik Sentinel-2 di Oregon, Amerika Serikat, sehingga memerlukan waktu lebih lama untuk dimuat.
    """,
    "keywords": [
        "sentinel",
        "sentinel-2",
        "sentinel 2",
        "sentinel-2a",
        "surface reflectance",
        "reflektansi permukaan",
        "s2_l2a",
    ],
    "name": "s2_l2a",
    "product_name": "s2_l2a",
    "default_time": "latest",
    "bands": SENTINEL2_BANDS,
    "native_crs": "EPSG:3857",
    "native_resolution": [10.0, -10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
    "styling": {
        "default_style": "simple_rgb",
        "styles": S2_ALL_STYLES,
    },
    "resource_limits": SENTINEL2_LIMITS,
    "feature_info": {
        "include_utc_dates": True,
        "include_bands": SENTINEL2_BANDS_INFO,
    },
    "time_resolution": "solar",
}
