# script para generar una funcion de prueba y luego aplicar la respuesta instrumental
import numpy as np
import matplotlib.pyplot as plt
from obspy import Trace, UTCDateTime
from obspy.io.sac.sacpz import attach_paz

# estos entradas son las frecuencas de los dos senos de la funcion de prueba
f1 = 2.0          # Hz, sine #1
f2 = 0.5          # Hz, sine #2
dt = 0.01         # s  (Fs = 1/dt)
npts = 1000        # numero de muestras
pz_file = "40T.pz"  # SACPZ file que debe estar en el directorio

# generar test function input
t = np.arange(npts) * dt
ut = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)      # arbitrary amplitude

tr = Trace(ut)
tr.stats.sampling_rate = 1.0/dt
tr.stats.starttime = UTCDateTime(0)

# leer los polos y ceros y generar la informacion de los polos y ceros
attach_paz(tr, paz_file=pz_file)     # generar tr.stats.paz desde 40T.pz
paz = tr.stats.paz                   # poles, zeros, ganancia
print(paz) 

# generar la traza del instrumento suponiendo que la entrada es desplazamiento del suelo
tr_instr = tr.copy().simulate(paz_simulate=paz) 

#alternativamente se puede suponer que la entrada es velocidad o aceleracion del suelo
#tr_instr = tr.copy().integrate().simulate(paz_simulate=tr.stats.paz)
#tr_instr = tr.copy().integrate().integrate().simulate(paz_simulate=tr.stats.paz)

# generar grafico de entrada y salida
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(9,5))
tt = tr.times(reftime=tr.stats.starttime)

# recuerde cambiar las unidades de input, dependiendo si son m, m/s o m/s/s
ax1.plot(tt, tr.data);      ax1.set_ylabel("input [m]")
ax2.plot(tt, tr_instr.data); ax2.set_ylabel("instrument output [counts]")
ax2.set_xlabel("Tiempo [s]")
ax1.grid(True); ax2.grid(True); fig.tight_layout() 
# guardar con un cierto nombre
plt.savefig('inputoutput_uaz.png')
plt.show()

