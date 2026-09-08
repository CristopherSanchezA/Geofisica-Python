#%%
import utm

def utm2lat_f(x, y, zone_number, zone_letter):
    # utm library automatically handles the ellipsoid WGS84
    lat, lon = utm.to_latlon(x, y, zone_number, zone_letter)
    # utm.to_latlon es una función en Python que convierte coordenadas UTM (Universal Transverse Mercator)
    # a coordenadas geográficas (latitud y longitud). Esta función es parte de la biblioteca utm.

    # WGS84 -> World Geodetic System 1984. Permite señalar cualquier punto que este situado en la tierra 
    # a través de tres unidades dadas (x,y,z) .
    
    return lat, lon

# %%
