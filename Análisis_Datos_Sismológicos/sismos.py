from obspy.clients.fdsn import Client
from obspy import UTCDateTime

client = Client("USGS")
ti = UTCDateTime("2026-09-27T18:55:00")
tf = UTCDateTime("2026-09-27T19:00:00")
catalogo = client.get_events(starttime=ti, endtime=tf, minmagnitude=4.0, 
                             minlatitude=-44, maxlatitude=-40, 
                             minlongitude=-75, maxlongitude=-70)

print(catalogo)
catalogo.plot()