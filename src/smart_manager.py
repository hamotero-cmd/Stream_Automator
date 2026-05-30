import os

def main():
    print("--- SMART M3U MANAGER ---")
    
    # Obtenemos el valor de la variable de entorno o usamos "Spain" por defecto
    filtro = os.getenv('PAIS_FILTRO', 'Spain')
    print(f"Filtrando por: {filtro}")
    
    # --- AQUÍ VA EL RESTO DE TU LÓGICA DE PROGRAMACIÓN ---
    # Ejemplo: 
    # lista = descargar_lista()
    # lista_filtrada = filtrar(lista, filtro)
    # guardar_archivo(lista_filtrada)
    
    print("Proceso finalizado correctamente.")

if __name__ == "__main__":
    main()