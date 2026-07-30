import numpy  # pylint: disable=import-error


def mask_by_nan(data, band):
    return ~numpy.isnan(data[band])


def mask_by_emad_nan(data, band):
    return ~numpy.isnan(data["EMAD"])


def bare_soil_index(data, swir, red, nir, blue):
    bsi = (data[swir] + data[red] - data[nir] - data[blue]) / (data[swir] + data[red] + data[nir] + data[blue])
    return bsi
