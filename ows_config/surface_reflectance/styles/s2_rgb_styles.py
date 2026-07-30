"""
RGB-based styles for Sentinel-2 Surface Reflectance
"""

s2_range = [0.0, 3000.0]

TRUE_COLOR = {
    "name": "simple_rgb",
    "title": "True Color - RGB",
    "abstract": "Komposit true color menggunakan band red, green, dan blue",
    "components": {
        "red": {"red": 1.0},
        "green": {"green": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": s2_range
}

FALSE_COLOR = {
    "name": "false_color",
    "title": "False Color - NIR, Red, Green",
    "abstract": "Komposit false color yang menonjolkan vegetasi",
    "components": {
        "red": {"nir": 1.0},    # NIR (B08)
        "green": {"red": 1.0},  # Red (B04)
        "blue": {"green": 1.0}  # Green (B03)
    },
    "scale_range": s2_range
}

INFRARED_GREEN = {
    "name": "infrared_green",
    "title": "False Color - SWIR, NIR, Green",
    "abstract": "Komposit false color menggunakan band SWIR 1, NIR, dan green",
    "components": {
        "red": {"swir_1": 1.0},   # SWIR1 (B11)
        "green": {"nir": 1.0},    # NIR (B08)
        "blue": {"green": 1.0}    # Green (B03)
    },
    "scale_range": s2_range
}

AGRICULTURE = {
    "name": "agriculture",
    "title": "Agriculture - SWIR, NIR, Blue",
    "abstract": "Komposit agrikultur menggunakan band SWIR 1, NIR, dan blue",
    "components": {
        "red": {"swir_1": 1.0},   # SWIR1 (B11)
        "green": {"nir": 1.0},    # NIR (B08)
        "blue": {"blue": 1.0}     # Blue (B02)
    },
    "scale_range": s2_range
}

ATMOSPHERIC_PENETRATION = {
    "name": "atmospheric_penetration",
    "title": "Atmospheric Penetration - SWIR2, SWIR1, Red",
    "abstract": "Komposit SWIR untuk penetrasi atmosfer dan deteksi asap",
    "components": {
        "red": {"swir_2": 1.0},   # SWIR2 (B12)
        "green": {"swir_1": 1.0}, # SWIR1 (B11)
        "blue": {"red": 1.0}      # Red (B04)
    },
    "scale_range": s2_range
}

BLUE_BAND = {
    "name": "blue",
    "title": "Blue - 490nm",
    "abstract": "Band blue (B02), 490 nm",
    "components": {
        "red": {"blue": 1.0},
        "green": {"blue": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": s2_range
}

GREEN_BAND = {
    "name": "green",
    "title": "Green - 560nm",
    "abstract": "Band green (B03), 560 nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0}
    },
    "scale_range": s2_range
}

RED_BAND = {
    "name": "red",
    "title": "Red - 665nm",
    "abstract": "Band red (B04), 665 nm",
    "components": {
        "red": {"red": 1.0},
        "green": {"red": 1.0},
        "blue": {"red": 1.0}
    },
    "scale_range": s2_range
}

NIR_BAND = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 842nm",
    "abstract": "Band near infrared (B08), 842 nm",
    "components": {
        "red": {"nir": 1.0},
        "green": {"nir": 1.0},
        "blue": {"nir": 1.0}
    },
    "scale_range": s2_range
}

SWIR1_BAND = {
    "name": "swir_1",
    "title": "SWIR 1 - 1610nm",
    "abstract": "Band short-wave infrared 1 (B11), 1610 nm",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"swir_1": 1.0},
        "blue": {"swir_1": 1.0}
    },
    "scale_range": s2_range
}

SWIR2_BAND = {
    "name": "swir_2",
    "title": "SWIR 2 - 2190nm",
    "abstract": "Band short-wave infrared 2 (B12), 2190 nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0}
    },
    "scale_range": s2_range
}

RED_EDGE_1 = {
    "name": "red_edge_1",
    "title": "Red Edge 1 - 705nm",
    "abstract": "Band vegetation red edge (B05), 705 nm",
    "components": {
        "red": {"red_edge_1": 1.0},
        "green": {"red_edge_1": 1.0},
        "blue": {"red_edge_1": 1.0}
    },
    "scale_range": s2_range
}

RED_EDGE_2 = {
    "name": "red_edge_2",
    "title": "Red Edge 2 - 740nm",
    "abstract": "Band vegetation red edge (B06), 740 nm",
    "components": {
        "red": {"red_edge_2": 1.0},
        "green": {"red_edge_2": 1.0},
        "blue": {"red_edge_2": 1.0}
    },
    "scale_range": s2_range
}

RED_EDGE_3 = {
    "name": "red_edge_3",
    "title": "Red Edge 3 - 783nm",
    "abstract": "Band vegetation red edge (B07), 783 nm",
    "components": {
        "red": {"red_edge_3": 1.0},
        "green": {"red_edge_3": 1.0},
        "blue": {"red_edge_3": 1.0}
    },
    "scale_range": s2_range
}

S2_RGB_STYLES = [
    TRUE_COLOR,
    FALSE_COLOR,
    INFRARED_GREEN,
    AGRICULTURE,
    ATMOSPHERIC_PENETRATION,
    BLUE_BAND,
    GREEN_BAND,
    RED_BAND,
    RED_EDGE_1,
    RED_EDGE_2,
    RED_EDGE_3,
    NIR_BAND,
    SWIR1_BAND,
    SWIR2_BAND,
]
