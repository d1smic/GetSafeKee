import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# se envia cada 1 de mes a las 9 de la mañana con el programador de tareas

EMAIL        = "abdelhakkasrioui5@gmail.com"          
APP_PASSWORD = "otjw jujh eiju rike"  # contraseña de aplicacion
DESTINATARIO = "manel.miliann@gmail.com" # a quién enviar

def construir_email() -> MIMEMultipart:
    msg = MIMEMultipart()
    msg["From"]    = EMAIL
    msg["To"]      = DESTINATARIO
    msg["Subject"] = "Recordatorio mensual: cambia tus contraseñas"

    cuerpo = f"""
    Hola,

    Este es tu recordatorio mensual para cambiar tus contraseñas.
    Fecha: {datetime.now().strftime("%d/%m/%Y")}

    Recomendaciones:
    - Cambia las contraseñas más importantes
    - Usa contraseñas de al menos 16 caracteres
    - No repitas contraseñas entre sitios

    -- Gestor de contraseñas
    """

    msg.attach(MIMEText(cuerpo, "plain"))
    return msg

def enviar_recordatorio():
    try:
        msg = construir_email()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.send_message(msg)

        print(f"✓ Email enviado: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    enviar_recordatorio()
