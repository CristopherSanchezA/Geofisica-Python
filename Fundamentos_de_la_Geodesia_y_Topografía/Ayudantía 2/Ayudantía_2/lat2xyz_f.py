import numpy as np

def lat2xyz_f(lon, lat, up):
    # 'up' está en km
    a = np.pi * lon / 180  # Convertir longitud a radianes
    b = np.pi * lat / 180  # Convertir latitud a radianes
    c = 6341 + up  # Radio de la Tierra en km + altura
    
    # Conversión de lat, lon y up a coordenadas cartesianas x, y, z.
    x = np.cos(b) * np.cos(a) * c
    y = np.cos(b) * np.sin(a) * c
    z = np.sin(b) * c
    
    return x, y, z
