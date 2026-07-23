# inadc-ows

[![Tests](https://github.com/piksel-ina/inadc-ows/actions/workflows/test.yml/badge.svg)](https://github.com/piksel-ina/inadc-ows/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![OGC](https://img.shields.io/badge/OGC-WMS%20%2F%20WCS-blue)](https://www.ogc.org/)

OWS (OGC Web Services) for the Indonesia datacube platform, powered by [datacube-ows](https://github.com/opendatacube/datacube-ows).

Requires a PostGIS database with ODC initialised and products indexed. For a quick setup with pre-configured products, use [piksel-core](https://github.com/piksel-ina/piksel-core) — once it's running:

    make build
    make up
    make init

## CI

Push a tag matching `inadc-ows-vYYYYMMDD-HHMM` to trigger an image build to ECR.




## Test requests

```bash
# Zoomed in - lowres
curl -o zoomed_in_lowres.png -m 60 \
"http://localhost:8000/?service=WMS&version=1.3.0&request=GetMap&layers=s2_geomad_annual_120&format=image/png&width=512&height=512&crs=EPSG:6933&bbox=10306772.1183124,-787968.478972056,10308650.2387255,-785644.211438856&time=2025-01-01"
# Looks good and returns in 3s.

# zoomed in - fullres
curl -o zoomed_in_fullres.png -m 60 \
"http://localhost:8000/?service=WMS&version=1.3.0&request=GetMap&layers=s2_geomad_annual_spectral&format=image/png&width=512&height=512&crs=EPSG:6933&bbox=10306772.1183124,-787968.478972056,10308650.2387255,-785644.211438856&time=2025-01-01"
# Looks good and returns in 4s.

# Zoomed out - lowres
curl -o zoomed_out_lowres.png -m 60 \
"http://localhost:8000/?service=WMS&version=1.3.0&request=GetMap&layers=s2_geomad_annual_120&format=image/png&width=512&height=512&crs=EPSG:6933&bbox=9865261.78358675,-1382377.46792413,12253528.180262,46846.6166830986&time=2025-01-01"
# Looks good and returns in 4s.

# Zoomed out - fullres
curl -o zoomed_out_fullres.png -m 60 \
"http://localhost:8000/?service=WMS&version=1.3.0&request=GetMap&layers=s2_geomad_annual_spectral&format=image/png&width=512&height=512&crs=EPSG:6933&bbox=9865261.78358675,-1382377.46792413,12253528.180262,46846.6166830986&time=2025-01-01"
# Didn't return after 60s. Should be as fast as lowres because it should return the same data. Switch setting to lowres isn't working.
```