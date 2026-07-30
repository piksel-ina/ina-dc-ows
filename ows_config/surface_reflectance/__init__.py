"""
Surface reflectance product configurations
"""

from .products.s2_l2a_sr import s2_l2a_layer
from .products.s2_geomad import (
    s2_geomad_annual_spectral_layer,
    s2_geomad_annual_indices_layer,
    s2_geomad_annual_statistics_layer,
)
from .products.landsat_c2l2_sr import landsat_c2l2_sr_folder

def get_surface_reflectance_layers():
    """Get all surface reflectance layers"""
    return [
        s2_l2a_layer,
        s2_geomad_annual_spectral_layer,
        s2_geomad_annual_indices_layer,
        s2_geomad_annual_statistics_layer,
        landsat_c2l2_sr_folder,
    ]

__all__ = ['get_surface_reflectance_layers']
