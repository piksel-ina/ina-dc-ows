"""
Styles for the Flood Hazard (Bahaya Banjir 2025) products.

Three measurements, three jobs, three deliberately distinct palettes:

- ``hazard_class`` is the producer's own low/moderate/high call and the default
  view. It is not derivable from either continuous band -- the class ranges
  overlap heavily on both index and depth -- so it gets the conventional
  yellow/orange/red hazard idiom and is treated as the authoritative answer.
- ``flood_depth`` is a physical measurement in metres, so its ramp is absolute
  and identical across all five return periods: the same colour always means the
  same depth, which is what makes rp02 and rp50 comparable. Blues, because it is
  water.
- ``hazard_index`` is a unitless relative score with no physical meaning, so no
  ramp is more "correct" than another. Breakpoints are therefore spaced by where
  the data actually sits (84% of valid pixels fall below 0.05) rather than
  evenly, which is what keeps low-hazard areas visible at all.
"""

_HAZARD_CLASS_COLOURS = {
    "low": "#ffeda0",
    "moderate": "#feb24c",
    "high": "#f03b20",
}

FLOOD_HAZARD_CLASS = {
    "name": "hazard_class",
    "title": "Flood Hazard Class",
    "abstract": "Flood hazard classified as low, moderate or high.",
    "value_map": {
        "flood_hazard_class": [
            {
                "title": "High",
                "abstract": "High flood hazard",
                "flags": {"hazard": "high"},
                "color": _HAZARD_CLASS_COLOURS["high"],
            },
            {
                "title": "Moderate",
                "abstract": "Moderate flood hazard",
                "flags": {"hazard": "moderate"},
                "color": _HAZARD_CLASS_COLOURS["moderate"],
            },
            {
                "title": "Low",
                "abstract": "Low flood hazard",
                "flags": {"hazard": "low"},
                "color": _HAZARD_CLASS_COLOURS["low"],
            },
        ]
    },
    "legend": {
        "width": 2.6,
        "height": 1.1,
    },
}

FLOOD_DEPTH = {
    "name": "flood_depth",
    "title": "Flood Depth (m)",
    "abstract": "Modelled flood depth in metres. Scale is identical across all "
                "return periods so depths can be compared between scenarios.",
    "needed_bands": ["flood_depth"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "flood_depth"},
    },
    "color_ramp": [
        # Same reasoning as the index style: keep the modelled footprint visible
        # even where depth rounds to nothing.
        {"value": 0.0, "color": "#f7fbff", "alpha": 0.35},
        {"value": 0.05, "color": "#deebf7", "alpha": 0.75},
        {"value": 0.10, "color": "#c6dbef"},
        {"value": 0.25, "color": "#9ecae1"},
        {"value": 0.50, "color": "#6baed6"},
        {"value": 0.75, "color": "#4292c6"},
        {"value": 1.00, "color": "#2171b5"},
        {"value": 1.50, "color": "#08519c"},
        {"value": 2.00, "color": "#08306b"},
        {"value": 2.50, "color": "#041c3f"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 2.5,
        "ticks": [0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 2.5],
        "units": "m",
        "title": "Flood depth",
    },
}

FLOOD_HAZARD_INDEX = {
    "name": "hazard_index",
    "title": "Flood Hazard Index",
    "abstract": "Relative flood hazard index, 0 to 1. Unitless -- it ranks "
                "locations against each other rather than measuring a quantity. "
                "Colour steps are closely spaced at the low end because most "
                "values sit near zero.",
    "needed_bands": ["flood_hazard_index"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "flood_hazard_index"},
    },
    "color_ramp": [
        # Near-zero is faint rather than transparent: coverage is a sparse
        # prototype, so "modelled, negligible hazard" has to stay
        # distinguishable from "not modelled at all".
        {"value": 0.00, "color": "#f7f4f9", "alpha": 0.35},
        {"value": 0.01, "color": "#e7e1ef", "alpha": 0.75},
        {"value": 0.05, "color": "#d4b9da"},
        {"value": 0.10, "color": "#c994c7"},
        {"value": 0.20, "color": "#df65b0"},
        {"value": 0.35, "color": "#e7298a"},
        {"value": 0.55, "color": "#ce1256"},
        {"value": 0.75, "color": "#980043"},
        {"value": 0.90, "color": "#67001f"},
    ],
    "legend": {
        "begin": 0.0,
        "end": 0.9,
        "ticks": [0.0, 0.05, 0.2, 0.55, 0.9],
        "title": "Hazard index",
    },
}

FLOOD_HAZARD_STYLES = [
    FLOOD_HAZARD_CLASS,
    FLOOD_DEPTH,
    FLOOD_HAZARD_INDEX,
]
