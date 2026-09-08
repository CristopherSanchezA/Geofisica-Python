#%%
# Desafío 2, complete el código.
# Se deben importar las funciones creadas
import numpy as np
from lat2utm_f import lat2utm_f  # Importar desde el archivo lat2utm_f.py
from lat2xyz_f import lat2xyz_f  # Importar desde el archivo lat2xyz_f.py
from xyz2lat_f import xyz2lat_f  # Importar desde el archivo xyz2lat_f.py


# Cargamos los datos del archivo gps.txt
gps = np.loadtxt('gps.txt')

# Aplicamos un corte para eliminar latitudes mayores a -68
cut = gps[:, 0] > -68
gps = gps[~cut, :]  # Mantenemos solo las filas donde la latitud es <= -68

# Se debe vectorizar la función para usar un conglomerado de puntos correspondiente a gps.txt

vector_lat2utm = np.vectorize(lat2utm_f)

# Llamamos función lat2utm para convertir latitud y longitud a coordenadas UTM


# Llamamos función lat2xyz_f para convertir latitud, longitud y altura a coordenadas XYZ. La altura z en km (gps[:, 2]* 0.001)


# Llamamos a la función xyz2lat_f para convertir coordenadas XYZ de nuevo a latitud, longitud y altura


# Probamos en un punto específico de GPS

print(f"Coordenadas UTM: {ux[1]}, {uy[1]}")
print(f"Coordenadas XYZ: {x[1]}, {y[1]}, {z[1]}")
print(f"Latitud: {lat[1]}, Longitud: {lon[1]}, Altura: {up[1]} km")
print(f"Zona UTM: {zone[1]}")

# %%
