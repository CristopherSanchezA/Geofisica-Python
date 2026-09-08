#%%
import utm

def lat2utm_f(lon, lat):
    # Convertir latitud/longitud a coordenadas UTM
    ux, uy, zone_number, zone_letter = utm.from_latlon(lat, lon)
    
    # Combinar el número de la zona y la letra
    zone = f"{zone_number}{zone_letter}"
    
    return float(ux), float(uy), zone
