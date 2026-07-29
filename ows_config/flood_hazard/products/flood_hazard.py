"""
Flood Hazard (Bahaya Banjir 2025) product configuration.

Return period is modelled as one product per scenario rather than a time axis or
an extra dimension, so each return period surfaces as its own named WMS layer.
The five layers are grouped in a single folder so clients can present them as a
scenario selector (TerriaMap ``modelDimensions``) rather than a time slider.
"""

from ...common.resource_limits import FLOOD_HAZARD_LIMIT
from ..bands.flood_hazard import FLOOD_HAZARD_BANDS, FLOOD_HAZARD_BANDS_INFO
from ..styles.flood_hazard import FLOOD_HAZARD_STYLES

_FLOOD_HAZARD_ABSTRACT = """
Flood hazard for {label} ({aep} annual exceedance probability), derived from a
Modified Geomorphic Flood Index over FABDEM v1.2 terrain with BMKG design
rainfall. Single 2025 epoch.

Three measurements are available as styles: hazard class (low / moderate / high),
modelled flood depth in metres, and the underlying relative hazard index. Hazard
class is the authoritative interpretation and is the default view.

Coverage note: this is a prototype release covering selected regions of Java
only, not the whole island. Areas outside the modelled regions carry no data
rather than zero hazard.
"""

# Return period -> (layer suffix, human label, annual exceedance probability)
_RETURN_PERIODS = [
    (2, "rp02", "a 1-in-2-year flood", "50%"),
    (5, "rp05", "a 1-in-5-year flood", "20%"),
    (10, "rp10", "a 1-in-10-year flood", "10%"),
    (25, "rp25", "a 1-in-25-year flood", "4%"),
    (50, "rp50", "a 1-in-50-year flood", "2%"),
]


def _build_layer(return_period, suffix, label, aep):
    return {
        "title": f"Bahaya Banjir 2025 - {return_period} year return period ({aep} AEP)",
        "name": f"flood_hazard_{suffix}",
        "abstract": _FLOOD_HAZARD_ABSTRACT.format(label=label, aep=aep),
        "product_name": f"flood_hazard_{suffix}",
        "bands": FLOOD_HAZARD_BANDS,
        "resource_limits": FLOOD_HAZARD_LIMIT,
        "dynamic": False,
        "time_resolution": "summary",
        "default_time": "latest",
        "native_crs": "EPSG:6933",
        "native_resolution": [30, -30],
        "image_processing": {
            # Nodata is NaN in the float bands, so the usual mask_by_val
            # comparison would pass it through (NaN != NaN is true).
            "extent_mask_func": ["ows_config.common.band_utils.mask_by_nan"],
            "always_fetch_bands": [],
            "manual_merge": False,
            "apply_solar_corrections": False,
        },
        # All three measurements are returned on click regardless of the style in
        # view, so one query answers "how deep, how hazardous, which class".
        "feature_info": {
            "include_utc_dates": False,
            "include_bands": FLOOD_HAZARD_BANDS_INFO,
        },
        "styling": {
            "default_style": "hazard_class",
            "styles": FLOOD_HAZARD_STYLES,
        },
    }


flood_hazard_layers = [
    _build_layer(rp, suffix, label, aep)
    for rp, suffix, label, aep in _RETURN_PERIODS
]

flood_hazard_folder = {
    "title": "Bahaya Banjir 2025 (Flood Hazard 2025)",
    "abstract": """
                Flood hazard scenarios for Indonesia, 2025. Five return periods
                (2, 5, 10, 25 and 50 years) are published as separate layers,
                each offering hazard class, flood depth and hazard index.

                Prototype release: selected regions of Java only.
                """,
    "keywords": ["flood", "banjir", "hazard", "bahaya", "inundation"],
    "layers": flood_hazard_layers,
}
