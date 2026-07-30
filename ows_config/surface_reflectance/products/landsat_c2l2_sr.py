"""
Landsat Collection 2 Level-2 Surface Reflectance product configuration
"""

from ...common.resource_limits import LANDSAT_LIMITS
from ..bands.landsat_bands import (
    LANDSAT_TM_BANDS,
    LANDSAT_TM_BANDS_INFO,
    LANDSAT_OLI_BANDS,
    LANDSAT_OLI_BANDS_INFO,
)
from ..styles import (
    LANDSAT_RGB_STYLES,
    LANDSAT_OLI_RGB_EXTRA,
    LANDSAT_INDEX_STYLES,
    LANDSAT_TM_PQ_STYLE,
    LANDSAT_OLI_PQ_STYLE,
)

_USGS_ATTRIBUTION = (
    "Landsat Level-2 Surface Reflectance Science Product courtesy of the "
    "U.S. Geological Survey."
)

_ABSTRACT_INTRO = (
    "Reflektansi permukaan (surface reflectance) adalah proporsi radiasi matahari"
    " yang dipantulkan permukaan bumi setelah pengaruh atmosfer dikoreksi,"
    " sehingga nilainya dapat dibandingkan antarwaktu dan antarlokasi."
)

_ABSTRACT_SOURCE = (
    "Data berasal dari sensor {sensor} di satelit {satellite}, koleksi USGS"
    " Landsat Collection 2 Level-2, dengan resolusi spasial 30 meter. Data dibaca"
    " langsung dari arsip publik USGS di Oregon, Amerika Serikat, sehingga"
    " memerlukan waktu lebih lama untuk dimuat."
)

_ABSTRACT_COVERAGE = "Data yang tersedia untuk Indonesia mencakup periode {coverage}."

_LS7_SLC_WARNING = (
    "Perhatian: scan line corrector (SLC) pada sensor ETM+ gagal berfungsi sejak"
    " 31 Mei 2003, sehingga setiap citra setelah tanggal tersebut memiliki celah"
    " data diagonal permanen yang mencakup sekitar 22% luas citra."
)

_SATELLITES = [
    {
        "product": "ls5_c2l2_sr",
        "title": "Landsat 5 (TM) Surface Reflectance",
        "satellite": "Landsat 5",
        "sensor": "TM (Thematic Mapper)",
        "coverage": "1986–2011",
        "keywords": ["landsat-5", "landsat 5", "ls5", "tm", "thematic mapper"],
        "bands": LANDSAT_TM_BANDS,
        "bands_info": LANDSAT_TM_BANDS_INFO,
        "styles": LANDSAT_RGB_STYLES + LANDSAT_INDEX_STYLES + [LANDSAT_TM_PQ_STYLE],
    },
    {
        "product": "ls7_c2l2_sr",
        "title": "Landsat 7 (ETM+) Surface Reflectance",
        "satellite": "Landsat 7",
        "sensor": "ETM+ (Enhanced Thematic Mapper Plus)",
        "coverage": "1999–2024",
        "warning": _LS7_SLC_WARNING,
        "keywords": ["landsat-7", "landsat 7", "ls7", "etm+", "etm"],
        "bands": LANDSAT_TM_BANDS,
        "bands_info": LANDSAT_TM_BANDS_INFO,
        "styles": LANDSAT_RGB_STYLES + LANDSAT_INDEX_STYLES + [LANDSAT_TM_PQ_STYLE],
    },
    {
        "product": "ls8_c2l2_sr",
        "title": "Landsat 8 (OLI/TIRS) Surface Reflectance",
        "satellite": "Landsat 8",
        "sensor": "OLI/TIRS (Operational Land Imager / Thermal Infrared Sensor)",
        "coverage": "2013–sekarang",
        "keywords": ["landsat-8", "landsat 8", "ls8", "oli", "tirs"],
        "bands": LANDSAT_OLI_BANDS,
        "bands_info": LANDSAT_OLI_BANDS_INFO,
        "styles": (
            LANDSAT_RGB_STYLES
            + LANDSAT_OLI_RGB_EXTRA
            + LANDSAT_INDEX_STYLES
            + [LANDSAT_OLI_PQ_STYLE]
        ),
    },
    {
        "product": "ls9_c2l2_sr",
        "title": "Landsat 9 (OLI-2/TIRS-2) Surface Reflectance",
        "satellite": "Landsat 9",
        "sensor": "OLI-2/TIRS-2 (Operational Land Imager 2 / Thermal Infrared Sensor 2)",
        "coverage": "2021–sekarang",
        "keywords": ["landsat-9", "landsat 9", "ls9", "oli-2", "tirs-2"],
        "bands": LANDSAT_OLI_BANDS,
        "bands_info": LANDSAT_OLI_BANDS_INFO,
        "styles": (
            LANDSAT_RGB_STYLES
            + LANDSAT_OLI_RGB_EXTRA
            + LANDSAT_INDEX_STYLES
            + [LANDSAT_OLI_PQ_STYLE]
        ),
    },
]


def _abstract(spec):
    paragraphs = [
        _ABSTRACT_INTRO,
        _ABSTRACT_SOURCE.format(sensor=spec["sensor"], satellite=spec["satellite"]),
        _ABSTRACT_COVERAGE.format(coverage=spec["coverage"]),
    ]
    if "warning" in spec:
        paragraphs.append(spec["warning"])
    paragraphs.append(_USGS_ATTRIBUTION)
    return "\n\n".join(paragraphs)


def _build_layer(spec):
    return {
        "title": spec["title"],
        "name": spec["product"],
        "product_name": spec["product"],
        "abstract": _abstract(spec),
        "keywords": spec["keywords"] + [
            "landsat",
            "surface reflectance",
            "reflektansi permukaan",
            spec["product"],
        ],
        "bands": spec["bands"],
        "native_crs": "EPSG:3857",
        "native_resolution": [30.0, -30.0],
        "resource_limits": LANDSAT_LIMITS,
        "dynamic": True,
        "time_resolution": "solar",
        "default_time": "latest",
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
            "always_fetch_bands": [],
            "manual_merge": False,
            "apply_solar_corrections": False,
        },
        "feature_info": {
            "include_utc_dates": True,
            "include_bands": spec["bands_info"],
        },
        "styling": {
            "default_style": "simple_rgb",
            "styles": spec["styles"],
        },
    }


_LAYERS_BY_PRODUCT = {
    spec["product"]: _build_layer(spec) for spec in _SATELLITES
}

landsat_c2l2_sr_layers = [
    _LAYERS_BY_PRODUCT["ls9_c2l2_sr"],
    _LAYERS_BY_PRODUCT["ls8_c2l2_sr"],
    _LAYERS_BY_PRODUCT["ls7_c2l2_sr"],
    _LAYERS_BY_PRODUCT["ls5_c2l2_sr"],
]

landsat_c2l2_sr_folder = {
    "title": "Landsat Surface Reflectance",
    "abstract": "\n\n".join([
        "Arsip reflektansi permukaan USGS Landsat Collection 2 Level-2 untuk"
        " Indonesia dengan resolusi 30 meter, mencakup periode 1986\u2013sekarang"
        " dari Landsat 5, 7, 8, dan 9.",
        "Setiap satelit diterbitkan sebagai produk tersendiri karena susunan band"
        " dan radiometri berbeda antargenerasi sensor, sehingga keempatnya tidak"
        " digabungkan menjadi satu deret waktu.",
        _USGS_ATTRIBUTION,
    ]),
    "keywords": [
        "landsat",
        "surface reflectance",
        "reflektansi permukaan",
        "usgs",
        "collection 2",
        "level-2",
    ],
    "layers": landsat_c2l2_sr_layers,
}
