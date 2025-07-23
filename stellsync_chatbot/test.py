import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = 'smtp.privateemail.com'
SMTP_PORT = 465
SMTP_USERNAME = 'info@stellsync.com'
SMTP_PASSWORD = 'StellSync@2025'  # Replace with your new application password

# Email details
msg = MIMEText("This is a test email to verify SMTP credentials.")
msg['Subject'] = 'SMTP Credential Test'
msg['From'] = SMTP_USERNAME
msg['To'] = 'jsenarathhh@gmail.com'  # Replace with your test email

try:
    # Connect to the SMTP server
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        # Log in with credentials
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        # Send the email
        server.send_message(msg)
    print("Email sent successfully! Credentials are valid.")
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")