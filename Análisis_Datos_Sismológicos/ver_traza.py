from obspy import read

tr = read("ruido_TRANB.HHZ")[0]
print(tr.stats)
tr.plot()
tr_filtered = tr.copy()
tr_filtered.detrend("demean"); tr_filtered.detrend("linear"); tr_filtered.taper(0.05, type="cosine")
tr_filtered.plot()