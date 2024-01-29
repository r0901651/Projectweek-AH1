#!/usr/bin/python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Replace with your SendGrid API key
sendgrid_api_key = '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'

sender_email = 'AH1checkin@gmail.com'

def incheck(r_nummer, examen, tijd):
    sendgrid_api_key = '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'
    sender_email = 'AH1checkin@gmail.com'
    recipient_email = r_nummer + '@student.thomasmore.be'
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject='Incheck mail ' + examen,
        plain_text_content='You have successfully checked in for the ' + examen + ' exam!' + '\n' + 'Time: ' + tijd
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Successfully sent email. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

def uitcheck(r_nummer, examen, tijd):
    sendgrid_api_key = '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'
    sender_email = 'AH1checkin@gmail.com'
    recipient_email = r_nummer + '@student.thomasmore.be'
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject='Uitcheck mail ' + examen,
        plain_text_content='You have successfully checked out for the ' + examen + ' exam!' + '\n' + 'Time: ' + tijd
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Successfully sent email. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")