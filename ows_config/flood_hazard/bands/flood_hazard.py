"""
Band definitions for the Flood Hazard (Bahaya Banjir 2025) products
"""

FLOOD_HAZARD_BANDS_INFO = {
    "flood_depth": "Flood depth (metres)",
    "flood_hazard_index": "Flood hazard index (0-1, relative)",
    "flood_hazard_class": "Flood hazard class (low / moderate / high)",
}

FLOOD_HAZARD_BANDS = {
    "flood_depth": ["flood_depth", "depth"],
    "flood_hazard_index": ["flood_hazard_index", "index", "hazard_index"],
    "flood_hazard_class": ["flood_hazard_class", "classified", "hazard_class"],
}
