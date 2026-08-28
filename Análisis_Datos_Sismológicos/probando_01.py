# %%
import numpy as np
from obspy import Trace, UTCDateTime
dt = 0.01 # delta en segundos (=> Fs = 100 Hz)
npts = 1000 # n´umero de muestras (~10 s)
t = np.arange(npts) * dt
f = 2.0
sine = np.sin(2*np.pi*f*t)
tr_sine = Trace(sine)
tr_sine.stats.sampling_rate = 1.0/dt
tr_sine.stats.starttime = UTCDateTime.now()
tr_sine.plot()
tr_sine.write("seno.sac", format="SAC")
# %%
from obspy import read
a = read()
a_plot = a.plot()
# %% Importaciones y lectura de datos
from obspy import read
import numpy as np
import matplotlib.pyplot as plt

# Esto se lee una sola vez
st = read("*CCSP*.sac").sort(keys=["channel"])
trZ = st.select(channel="*Z")[0]
trN = st.select(channel="*N")[0]
trE = st.select(channel="*E")[0]

# %% Generar el gráfico
# Si quieres cambiar algo del gráfico, solo vuelves a ejecutar esta celda
plt.figure(figsize=(10,5))
t = trZ.times(reftime=trZ.stats.starttime)

plt.plot(t, trZ.data, label=trZ.id)
plt.plot(t, trN.data, label=trN.id)
plt.plot(t, trE.data, label=trE.id)

plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleración [cm/s/s]")
plt.title("Maule 2010 en CCSP")
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()

# Esto le dice a VS Code "imprime el gráfico en la ventana interactiva ahora"
plt.show()
# %%
