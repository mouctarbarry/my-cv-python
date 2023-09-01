from email.mime.text import MIMEText
import smtplib


def send_email(subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'barrymouctaar@gmail.com'
    smtp_password = 'wkhrlnvwwkbelnen'
    sender_email = 'barrymouctaar@gmail.com'
    recipient_email = 'bmouctar22@gmail.com'

    try:
        # Création du message MIME
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # Connexion au serveur SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Envoi de l'e-mail
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        return True
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
        return False


def submit_form(data):
    try:
        firstname = data.get('firstname')
        lastname = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        if not firstname or not lastname or not email or not message:
            response = {
                'success': False,
                'message': 'Tous les champs obligatoires doivent être remplis.'
            }
        else:
            subject = f"Message de {firstname} {lastname}"
            email_body = f"De : {firstname} {lastname}\nEmail : {email}\nTéléphone : {phone}\n\n{message}"

            if send_email(subject, email_body):
                response = {
                    'success': True,
                    'message': "L'e-mail a été envoyé avec succès."
                }
            else:
                response = {
                    'success': False,
                    'message': "Une erreur est survenue lors de l'envoi de l'e-mail."
                }

        return response

    except Exception as e:
        response = {
            'success': False,
            'message': f"Erreur : {e}"
        }
        return response
