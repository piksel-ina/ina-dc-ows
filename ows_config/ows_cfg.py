"""
Main OWS configuration entry point
"""
from .ows_root_cfg import (
    service_title,
    service_abstract,
    service_keywords,
    contact_info,
    published_CRSs,
    allowed_urls,
    services,
    wms,
    wcs,
    ENABLE_SURFACE_REFLECTANCE,
    ENABLE_FLOOD_HAZARD,
)

layers = []

if ENABLE_SURFACE_REFLECTANCE:
    from .surface_reflectance import get_surface_reflectance_layers
    layers.extend(get_surface_reflectance_layers())

if ENABLE_FLOOD_HAZARD:
    from .flood_hazard import get_flood_hazard_layers
    layers.extend(get_flood_hazard_layers())

ows_cfg = {
    "global": {
        "response_headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "info_url": "",
        "fees": "",
        "access_constraints": "",
        "title": service_title,
        "abstract": service_abstract,
        "keywords": service_keywords,
        "contact_info": contact_info,
        "published_CRSs": published_CRSs,
        "allowed_urls": allowed_urls,
        "services": services,
        "load_driver": "rio",
    },
    "wms": wms,
    "wcs": wcs,
    "layers": layers,
}

if __name__ == "__main__":
    def describe(layer, indent="  "):
        if "layers" in layer:
            print(f"{indent}[{layer['title']}]")
            for child in layer["layers"]:
                describe(child, indent + "  ")
            return
        print(f"{indent}- {layer['name']}: {layer['title']}")
        print(f"{indent}  Available Styles: {len(layer['styling']['styles'])}")
        print(f"{indent}  CRS: {layer['native_crs']}")
        print(f"{indent}  Resolution: {layer['native_resolution']}")
        print(f"{indent}  Default Style: {layer['styling']['default_style']}")

    print(f"Service: {service_title}")
    print(f"Top-level entries configured: {len(layers)}")
    for layer in layers:
        describe(layer)
