"""
Landsat Collection 2 Level-2 band definitions and metadata
"""

LANDSAT_TM_BANDS_INFO = {
    "blue": "Blue (450–520 nm)",
    "green": "Green (520–600 nm)",
    "red": "Red (630–690 nm)",
    "nir08": "NIR (760–900 nm)",
    "swir16": "SWIR 1 (1550–1750 nm)",
    "swir22": "SWIR 2 (2080–2350 nm)",
    "qa_pixel": "Pixel Quality Assessment - Informasi kualitas piksel",
    "atmos_opacity": "Atmospheric Opacity - Opasitas atmosfer",
    "cloud_qa": "Cloud Quality Assessment - Masker awan tambahan",
}

LANDSAT_TM_BANDS = {
    "blue": [],
    "green": [],
    "red": [],
    "nir08": ["nir"],
    "swir16": ["swir_1"],
    "swir22": ["swir_2"],
    "qa_pixel": ["pq", "pixel_quality"],
    "atmos_opacity": ["atmospheric_opacity"],
    "cloud_qa": [],
}

LANDSAT_OLI_BANDS_INFO = {
    "coastal": "Coastal aerosol (435–451 nm)",
    "blue": "Blue (452–512 nm)",
    "green": "Green (533–590 nm)",
    "red": "Red (636–673 nm)",
    "nir08": "NIR (851–879 nm)",
    "swir16": "SWIR 1 (1566–1651 nm)",
    "swir22": "SWIR 2 (2107–2294 nm)",
    "qa_pixel": "Pixel Quality Assessment - Informasi kualitas piksel",
    "qa_aerosol": "Aerosol Quality Assessment - Informasi kualitas aerosol",
}

LANDSAT_OLI_BANDS = {
    "coastal": ["coastal_aerosol"],
    "blue": [],
    "green": [],
    "red": [],
    "nir08": ["nir"],
    "swir16": ["swir_1"],
    "swir22": ["swir_2"],
    "qa_pixel": ["pq", "pixel_quality"],
    "qa_aerosol": ["aerosol_qa"],
}
