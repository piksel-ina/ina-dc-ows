"""
Flood hazard product configurations
"""

from .products.flood_hazard import flood_hazard_folder


def get_flood_hazard_layers():
    """Get all flood hazard layers, grouped under one folder."""
    return [flood_hazard_folder]


__all__ = ['get_flood_hazard_layers']
