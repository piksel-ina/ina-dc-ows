"""
Styles for Surface Reflectance products
"""

from .s2_rgb_styles import S2_RGB_STYLES
from .s2_index_styles import S2_INDEX_STYLES
from .landsat_rgb_styles import LANDSAT_RGB_STYLES, LANDSAT_OLI_RGB_EXTRA
from .landsat_index_styles import LANDSAT_INDEX_STYLES
from .landsat_pq_styles import LANDSAT_TM_PQ_STYLE, LANDSAT_OLI_PQ_STYLE

S2_ALL_STYLES = S2_RGB_STYLES + S2_INDEX_STYLES

__all__ = [
    'S2_RGB_STYLES',
    'S2_INDEX_STYLES',
    'S2_ALL_STYLES',
    'LANDSAT_RGB_STYLES',
    'LANDSAT_OLI_RGB_EXTRA',
    'LANDSAT_INDEX_STYLES',
    'LANDSAT_TM_PQ_STYLE',
    'LANDSAT_OLI_PQ_STYLE',
]
