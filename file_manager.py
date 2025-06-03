# ari
from datetime import datetime

def guardar_en_archivo(buffer, archivo_output="output.txt"):
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

        print(f"Archivo guardado como: {archivo_output}")
        return archivo_output
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return None
