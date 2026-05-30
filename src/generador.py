# Generador simple de lista M3U
# Esto crea un archivo .m3u que puedes abrir en VLC o cualquier reproductor IPTV

ruta_salida = r"E:\Stream_Automator\output\mi_lista.m3u"

contenido_m3u = """#EXTM3U
#EXTINF:-1, Canal de Prueba 1
http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
#EXTINF:-1, Canal de Prueba 2
https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8
"""

with open(ruta_salida, "w", encoding="utf-8") as archivo:
    archivo.write(contenido_m3u)

print("¡Éxito! El archivo se ha creado en: " + ruta_salida)