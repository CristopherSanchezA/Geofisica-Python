#%%
import pygmt

# Parámetros y archivos
grid_file = "gebco_2026_n39.5_s35.5_w135.5_e139.5.nc"  # Mayor resolución que ETOPO1
region = [135.5, 139.5, 35.5, 39.5]

# 1. Calcular sombreado de relieve optimizado
gradient = pygmt.grdgradient(grid=grid_file, azimuth=45, normalize="e0.6")

pygmt.makecpt(
    cmap="geo",
    series=[-3500, 3000, 500],
    continuous=True,
    output="mipaleta.cpt",
)

fig = pygmt.Figure()

# 2. Relieve sombreado en alta resolución
fig.grdimage(
    grid=grid_file,
    region=region,
    projection="M15c",
    cmap="mipaleta.cpt",
    shading=gradient,
)

# 3. Línea de costa en resolución 'full' y marco
fig.coast(
    resolution="f",
    shorelines="1/0.6p,black",
    frame=["a1f0.5", "WSen"],
)

# 4. Fosa / Límite de subducción
fig.plot(
    data="trench_japan_sea.txt",
    pen="1.2p,black",
    style="f0.3c/0.09c+r+t",  # Dientes ajustados a la escala
    fill="black",
    label="Borde convergente",
)

# 5. Largo de ruptura
fig.plot(
    data="largo_ruptura_noto.txt",
    pen="3p,orangeRed",  # Línea visible y llamativa
    # Si la prefieres discontinua/punteada: pen="3p,orangeRed,4_2:0p"
    label="Largo de ruptura (~150 km)",
)

# Epicentro Terremoto Noto 2024 (1 de enero de 2024, USGS: 37.498°N, 137.242°E)
fig.plot(
    x=[137.242],
    y=[37.498],
    style="a0.55c",        # Estrella ('a') de 0.55 cm
    fill="red",
    pen="0.6p,black",
    label="Epicentro Mww 7.5",
)

# Mapa de ubicación regional (Inset) en la esquina superior derecha
with fig.inset(position="jTR+w3.5c/4c+o0.3c/0.3c", box="+gwhite+p0.8p,black"):
    # Graficar archipiélago de Japón
    fig.coast(
        region=[128, 146, 30, 46],
        projection="M3.5c",
        land="lightgray",
        water="white",
        shorelines="1/0.2p,black",
    )
    # Rectángulo rojo de la zona de estudio
    fig.plot(data=[# [xmin, ymin, xmax, ymax] -> [135.5, 35.5, 139.5, 39.5]
fig.plot(data=[[135.5, 35.5, 139.5, 39.5]], style="r+s", pen="1.2p,red")], style="r+s", pen="1p,red")

# 8. Etiquetas geográficas con fuentes personalizadas
fig.text(
    x=[137.03, 138.41, 137.00],
    y=[36.73, 38.04, 38.80],
    text=["Península de Noto", "Isla Sado", "Mar de Japón"],
    font=[
        "8.5p,Helvetica-Bold,black",
        "8.5p,Helvetica-Bold,black",
        "11p,Helvetica-BoldOblique,navy",
    ],
    # Opcional: fondo semitransparente o halo para resaltar sobre el relieve
    fill="white@30",   # Le da una cajita blanca suave a cada texto
    clearance="0.1c",  # Margen interior de la cajita
)

fig.basemap(
    map_scale="jBL+w50k+o0.8c/0.8c+f+u",
    box="+gwhite@20+p0.5p,black",
)

# 3. Y en la barra de color llamar a la misma paleta:
fig.colorbar(
    cmap="mipaleta.cpt",
    frame=["a1000f500", "x+lElevación / Batimetría (m)"],
    position="JBR+jBR+o0.8c/0.8c+w5.5c/0.25c+h",
    box="+gwhite@20+p0.5p,black",
)

# 8. Leyenda con cuadro de fondo blanco para legibilidad
fig.legend(
    position="JTL+jTL+o0.3c/0.6c",
    box="+gwhite@15+p0.5p,black",  # Caja blanca con leve transparencia
)

# 9. Guardar en alta calidad (600 DPI)
fig.savefig("mapa_japon_hq.png", dpi=600)
# Exportar en PDF vectorial de máxima resolución
fig.savefig("mapa_japon_hq.pdf")
fig.show()
#%%
import pygmt

# Archivos y configuración
grid_file = "gebco_2026_n39.5_s35.5_w135.5_e139.5.nc"
region = [135.5, 139.5, 35.5, 39.5]

# 1. Paleta de colores acotada
pygmt.makecpt(
    cmap="geo",
    series=[-3500, 3000, 500],
    continuous=True,
    output="mipaleta.cpt",
)

# 2. Gradiente topográfico
gradient = pygmt.grdgradient(grid=grid_file, azimuth=45, normalize="e0.6")

fig = pygmt.Figure()

# Configuración global de fuentes y marco acorde a una columna (8.4 cm)
with pygmt.config(
    FONT_ANNOT_PRIMARY="7.5p,Helvetica,black",
    FONT_LABEL="8p,Helvetica,black",
    MAP_FRAME_WIDTH="2.5p",
):
    # 3. Mapa base ajustado a una columna (8.4 cm)
    fig.grdimage(
        grid=grid_file,
        region=region,
        projection="M8.4c",
        cmap="mipaleta.cpt",
        shading=gradient,
    )

    # 4. Costa y marco exterior
    fig.coast(
        resolution="f",
        shorelines="1/0.4p,black",
        frame=["a1f0.5", "WSen"],
    )

# 5. Borde convergente
fig.plot(
    data="trench_japan_sea.txt",
    pen="0.8p,black",
    style="f0.22c/0.06c+r+t",
    fill="black",
    label="Borde convergente",
)

# 6. Traza de la ruptura
fig.plot(
    data="largo_ruptura_noto.txt",
    pen="2p,orangeRed",
    label="Ruptura (~150 km)",
)

# 7. Epicentro Mw 7.5
fig.plot(
    x=[137.242],
    y=[37.498],
    style="a0.35c",
    fill="red",
    pen="0.4p,black",
    label="Epicentro Mww 7.5",
)

# 8. Etiquetas geográficas
fig.text(
    x=[137.05, 138.41, 137.00],
    y=[36.73, 38.04, 38.80],
    text=["Península de Noto", "Isla Sado", "Mar de Japón"],
    font=[
        "6.5p,Helvetica-Bold,black",
        "6.5p,Helvetica-Bold,black",
        "8.5p,Helvetica-BoldOblique,navy",
    ],
    fill="white@30",
    clearance="0.08c",
)

# 9. Inset map
with fig.inset(
    position="jTR+w2.0c/2.3c+o0.15c/0.15c", box="+gwhite+p0.4p,black"
):
    fig.coast(
        region=[128, 146, 30, 46],
        projection="M2.0c",
        land="lightgray",
        water="white",
        shorelines="1/0.15p,black",
    )
    # [xmin, ymin, xmax, ymax]
    fig.plot(data=[[135.5, 35.5, 139.5, 39.5]], style="r+s", pen="0.8p,red")

# 10, 11 y 12. Escala, Colorbar y Leyenda completamente dentro del marco
with pygmt.config(
    FONT_ANNOT_PRIMARY="6p,Helvetica,black",
    FONT_LABEL="6.5p,Helvetica,black",
    MAP_TICK_LENGTH_PRIMARY="1.5p",
    MAP_ANNOT_OFFSET_PRIMARY="2p",
    MAP_LABEL_OFFSET="3p",
):
    # 10. Escala gráfica: +jBL obliga a anclar desde su esquina inferior izquierda
    fig.basemap(
        map_scale="jBL+jBL+w50k+o0.4c/0.4c+f+u",
        box="+gwhite@15+p0.4p,black",
    )

    # 11. Barra de color: +jBR ancla su esquina y +o0.55c/0.75c da espacio al texto inferior
    fig.colorbar(
        cmap="mipaleta.cpt",
        frame=["a1500f500", "x+lElevación (m)"],
        position="jBR+jBR+o0.35c/0.45c+w2.6c/0.15c+h",
        box="+gwhite@15+p0.4p,black",
    )

    # 12. Leyenda
    fig.legend(
        position="jTL+jTL+o0.15c/0.15c",
        box="+gwhite@15+p0.4p,black",
    )

# 13. Guardar en formato vectorial PDF y PNG de prueba
fig.savefig("mapa_japon_columna.pdf")
fig.savefig("mapa_japon_columna.png", dpi=600)
fig.show()
# %%
