from datetime import datetime
import traceback

def guardar_en_archivo(buffer: str, archivo_output: str = "output.txt") -> str:
    """
    Genera un archivo de texto plano con:
      - Cabecera (fecha y separadores)
      - Contenido completo de 'buffer'
    Devuelve el nombre del archivo o None si hubo error.
    """
    try:
        contenido = "============= REGISTRO DE KEYLOGGER =============\n"
        contenido += f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        contenido += "=================================================\n"
        contenido += "Eventos registrados:\n"
        contenido += buffer
        contenido += "\n=================================================\n"
        contenido += "FIN DEL REGISTRO\n"

        with open(archivo_output, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)

        print(f"[file_manager] Archivo guardado como: {archivo_output}")
        return archivo_output

    except Exception:
        print("[file_manager] Error al guardar el archivo:")
        traceback.print_exc()
        return None
