"""
Surface reflectance product configurations
"""

from .products.s2_l2a_sr import s2_l2a_layer
from .products.s2_geomad import (
    s2_geomad_annual_spectral_layer,
    s2_geomad_annual_indices_layer,
    s2_geomad_annual_statistics_layer,
)
from .products.geomad_s2 import geomad_s2_annual_legacy_layer

def get_surface_reflectance_layers():
    """Get all surface reflectance layers"""
    return [
        s2_l2a_layer,
        s2_geomad_annual_spectral_layer,
        s2_geomad_annual_indices_layer,
        s2_geomad_annual_statistics_layer,
        geomad_s2_annual_legacy_layer,
    ]

__all__ = ['get_surface_reflectance_layers']
