#!/usr/bin/python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your SendGrid API key
sendgrid_api_key = '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'

sender_email = 'AH1checkin@gmail.com'
recipient_email = 'michiel.kuyken@gmail.com'

message = Mail(
    from_email=sender_email,
    to_emails=recipient_email,
    subject='Test mail',
    plain_text_content='This is a test mail'
)

try:
    sg = SendGridAPIClient(sendgrid_api_key)
    response = sg.send(message)
    print(f"Successfully sent email. Status Code: {response.status_code}")
except Exception as e:
    print(f"Error sending email: {str(e)}")
