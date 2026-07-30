"""
Styles for the Flood Hazard (Bahaya Banjir 2025) products.

Class and index both use the BNPB hazard palette. Depth keeps its own blues: it
is a physical measurement on an absolute scale, so the same colour means the
same depth across all five return periods, which is what makes them comparable.
"""

from ...common.legends import (
    HAZARD_CLASS_LEGEND,
    hazard_class_value_map,
    hazard_index_color_ramp,
)

FLOOD_HAZARD_CLASS = {
    "name": "hazard_class",
    "title": "Kelas Bahaya Banjir",
    "abstract": "Bahaya banjir yang diklasifikasikan menjadi rendah, sedang, atau tinggi.",
    "value_map": hazard_class_value_map("flood_hazard_class"),
    "legend": HAZARD_CLASS_LEGEND,
}

FLOOD_DEPTH = {
    "name": "flood_depth",
    "title": "Kedalaman Banjir (m)",
    "abstract": "Kedalaman banjir hasil pemodelan dalam meter.",
    "needed_bands": ["flood_depth"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "flood_depth"},
    },
    "color_ramp": [
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
        "begin": "0.0",
        "end": "2.5",
        "ticks": ["0.0", "0.25", "0.5", "1.0", "1.5", "2.0", "2.5"],
        "units": "m",
        "title": "Kedalaman banjir",
    },
}

FLOOD_HAZARD_INDEX = {
    "name": "hazard_index",
    "title": "Indeks Bahaya Banjir",
    "abstract": "Indeks bahaya banjir relatif dengan nilai 0 sampai 1, semakin "
                "tinggi nilainya semakin besar bahayanya, sehingga dapat "
                "digunakan untuk membandingkan tingkat bahaya antarlokasi.",
    "needed_bands": ["flood_hazard_index"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "flood_hazard_index"},
    },
    "color_ramp": hazard_index_color_ramp(
        [0.0, 0.167, 0.333, 0.5, 0.667, 0.833, 1.0]
    ),
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "ticks": ["0.0", "0.333", "0.667", "1.0"],
        "title": "Indeks bahaya",
    },
}

FLOOD_HAZARD_STYLES = [
    FLOOD_HAZARD_CLASS,
    FLOOD_DEPTH,
    FLOOD_HAZARD_INDEX,
]
