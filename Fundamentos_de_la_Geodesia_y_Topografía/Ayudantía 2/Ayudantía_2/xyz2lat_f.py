import numpy as np

def xyz2lat_f(x, y, z):
    # Conversión de coordenadas cartesianas a esféricas
    lon = np.degrees(np.arctan2(y, x))
    lat = np.degrees(np.arcsin(z / np.sqrt(x**2 + y**2 + z**2)))
    r = np.sqrt(x**2 + y**2 + z**2)
    up = (0.001 * r - 6341)  # Altura en km
    return lat, lon, up

