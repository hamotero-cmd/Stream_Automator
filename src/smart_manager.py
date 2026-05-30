import requests

def verificar_enlace(url):
    """Comprueba si un enlace responde correctamente."""
    try:
        # Usamos HEAD en lugar de GET porque es mucho más rápido
        # Solo pedimos los encabezados, no el video completo
        response = requests.head(url, timeout=3)
        return response.status_code == 200
    except:
        return False

def main():
    archivo_entrada = r"E:\Stream_Automator\output\lista_descargada.m3u"
    archivo_salida = r"E:\Stream_Automator\output\lista_inteligente.m3u"

    print("--- SMART M3U MANAGER ---")
    filtro = input("Introduce el país o palabra clave para filtrar (ej: Spain): ")
    validar = input("¿Quieres verificar si los enlaces funcionan? (s/n): ").lower()

    print(f"\nProcesando lista... esto puede tardar un poco.")
    
    try:
        with open(archivo_entrada, "r", encoding="utf-8") as entrada:
            lineas = entrada.readlines()

        with open(archivo_salida, "w", encoding="utf-8") as salida:
            salida.write("#EXTM3U\n")
            
            # Procesamos por pares (Info + URL)
            for i in range(len(lineas) - 1):
                if filtro in lineas[i]:
                    info_canal = lineas[i]
                    url_canal = lineas[i+1].strip()
                    
                    if validar == 's':
                        print(f"Verificando: {info_canal.strip()}...")
                        if verificar_enlace(url_canal):
                            salida.write(info_canal)
                            salida.write(url_canal + "\n")
                    else:
                        salida.write(info_canal)
                        salida.write(url_canal + "\n")

        print(f"\n¡Proceso terminado! Tu lista está en: {archivo_salida}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()