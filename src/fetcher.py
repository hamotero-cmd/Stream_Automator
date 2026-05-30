# Configuraciones
archivo_entrada = r"E:\Stream_Automator\output\lista_descargada.m3u"
archivo_salida = r"E:\Stream_Automator\output\mi_lista_personalizada.m3u"
filtro = "Spain" # Palabra que buscaremos en la lista

print(f"Filtrando canales que contienen: {filtro}...")

try:
    with open(archivo_entrada, "r", encoding="utf-8") as entrada, \
         open(archivo_salida, "w", encoding="utf-8") as salida:
        
        # Escribimos la cabecera necesaria para cualquier archivo M3U
        salida.write("#EXTM3U\n")
        
        lineas = entrada.readlines()
        
        # Procesamos la lista por pares (info del canal + URL)
        for i in range(len(lineas)):
            # Si encontramos el filtro en la línea actual
            if filtro in lineas[i]:
                # Guardamos la info del canal y el enlace (la línea siguiente)
                salida.write(lineas[i])
                salida.write(lineas[i+1])

    print(f"¡Listo! Lista limpia guardada en: {archivo_salida}")

except Exception as e:
    print(f"Error al procesar: {e}")