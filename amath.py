import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Mettez vos informations d'identification SMTP ici
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'votre_email@example.com'
    smtp_password = 'votre_mot_de_passe'

    # Construction du message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Connexion au serveur SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

# Utilisation de la fonction pour envoyer un email
send_email('Sujet de l'email', 'Corps de l\'email', 'destinataire@example.com')

