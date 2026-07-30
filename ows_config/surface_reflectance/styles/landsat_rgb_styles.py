"""
RGB-based styles for Landsat Collection 2 Level-2 Surface Reflectance
"""

LANDSAT_SCALE_RANGE = [7272.0, 18181.0]

TRUE_COLOR = {
    "name": "simple_rgb",
    "title": "True Color - RGB",
    "abstract": "Komposit true color menggunakan band red, green, dan blue",
    "components": {
        "red": {"red": 1.0},
        "green": {"green": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

FALSE_COLOR = {
    "name": "false_color",
    "title": "False Color - NIR, Red, Green",
    "abstract": "Komposit false color yang menonjolkan vegetasi",
    "components": {
        "red": {"nir": 1.0},
        "green": {"red": 1.0},
        "blue": {"green": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

INFRARED_GREEN = {
    "name": "infrared_green",
    "title": "False Color - SWIR, NIR, Green",
    "abstract": "Komposit false color menggunakan band SWIR 1, NIR, dan green",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

AGRICULTURE = {
    "name": "agriculture",
    "title": "Agriculture - SWIR, NIR, Blue",
    "abstract": "Komposit agrikultur menggunakan band SWIR 1, NIR, dan blue",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

ATMOSPHERIC_PENETRATION = {
    "name": "atmospheric_penetration",
    "title": "Atmospheric Penetration - SWIR2, SWIR1, Red",
    "abstract": "Komposit SWIR untuk penetrasi atmosfer dan deteksi asap",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_1": 1.0},
        "blue": {"red": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

COASTAL_BAND = {
    "name": "coastal",
    "title": "Coastal Aerosol",
    "abstract": "Band coastal aerosol (SR_B1)",
    "components": {
        "red": {"coastal": 1.0},
        "green": {"coastal": 1.0},
        "blue": {"coastal": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

BLUE_BAND = {
    "name": "blue",
    "title": "Blue",
    "abstract": "Band blue",
    "components": {
        "red": {"blue": 1.0},
        "green": {"blue": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

GREEN_BAND = {
    "name": "green",
    "title": "Green",
    "abstract": "Band green",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

RED_BAND = {
    "name": "red",
    "title": "Red",
    "abstract": "Band red",
    "components": {
        "red": {"red": 1.0},
        "green": {"red": 1.0},
        "blue": {"red": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

NIR_BAND = {
    "name": "nir",
    "title": "Near Infrared (NIR)",
    "abstract": "Band near infrared",
    "components": {
        "red": {"nir": 1.0},
        "green": {"nir": 1.0},
        "blue": {"nir": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

SWIR1_BAND = {
    "name": "swir_1",
    "title": "SWIR 1",
    "abstract": "Band short-wave infrared 1",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"swir_1": 1.0},
        "blue": {"swir_1": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

SWIR2_BAND = {
    "name": "swir_2",
    "title": "SWIR 2",
    "abstract": "Band short-wave infrared 2",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0}
    },
    "scale_range": LANDSAT_SCALE_RANGE
}

LANDSAT_RGB_STYLES = [
    TRUE_COLOR,
    FALSE_COLOR,
    INFRARED_GREEN,
    AGRICULTURE,
    ATMOSPHERIC_PENETRATION,
    BLUE_BAND,
    GREEN_BAND,
    RED_BAND,
    NIR_BAND,
    SWIR1_BAND,
    SWIR2_BAND,
]

LANDSAT_OLI_RGB_EXTRA = [COASTAL_BAND]
