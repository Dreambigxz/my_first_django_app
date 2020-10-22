import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(
    from_email='from_email@example.com',
    to_emails='onyemordidaniel@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

    print('Sent')
except Exception as e:
    pass
    print('e')