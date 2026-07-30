"""
Common resource limit configurations
"""

dataset_cache_rules = [
    {
        "min_datasets": 1,
        "max_age": 60 * 60 * 8,
    },
    {
        "min_datasets": 5,
        "max_age": 60 * 60 * 24,
    },
    {
        "min_datasets": 9,
        "max_age": 60 * 60 * 24 * 7,
    },
    {
        "min_datasets": 17,
        "max_age": 60 * 60 * 24 * 30,
    },
    {
        "min_datasets": 31,
        "max_age": 60 * 60 * 24 * 120,
    },
]

DEFAULT_LIMITS = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 35.0,
        "max_datasets": 6,
    },
    "wcs": {
        "max_datasets": 16,
    }
}

SENTINEL2_LIMITS = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 50.0,
        "max_datasets": 65,
        "dataset_cache_rules": dataset_cache_rules
    },
    "wcs": {
        "max_datasets": 65,
    }
}

LANDSAT_LIMITS = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 35.0,
        "max_datasets": 32,
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": {
        "max_datasets": 32,
    },
}

GEOMAD_S2_CACHE_RULES = [
    {"min_datasets": 5,  "max_age": 60 * 60 * 24 * 7},
    {"min_datasets": 9,  "max_age": 60 * 60 * 24 * 30},
    {"min_datasets": 17, "max_age": 60 * 60 * 24 * 90},
    {"min_datasets": 31, "max_age": 60 * 60 * 24 * 180},
]

GEOMAD_S2_LIMIT = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 8,
        "max_datasets": 32, # Needs to be greater than the min_datasets in the cache rules.
        "min_zoom_factor": 30.0,
        "dataset_cache_rules": GEOMAD_S2_CACHE_RULES,
    },
    "wcs": {
        "max_datasets": 32,
    },
}

FLOOD_HAZARD_CACHE_RULES = [
    {"min_datasets": 1, "max_age": 60 * 60 * 24 * 30},
]

FLOOD_HAZARD_LIMIT = {
    "wms": {
        "zoomed_out_fill_colour": [0, 0, 0, 0],
        "min_zoom_factor": 1.0,
        "max_datasets": 4,
        "dataset_cache_rules": FLOOD_HAZARD_CACHE_RULES,
    },
    "wcs": {
        "max_datasets": 4,
    },
}
