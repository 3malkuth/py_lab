from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# os.environ.get('SENDGRID_API_KEY') # could also use environment variables to access the API key

def send_email(str_from_email, str_to_emails, str_api_key, str_subject, str_html_content):
    mail_message = Mail(
        from_email=str_from_email,
        to_emails=str_to_emails,
        subject=str_subject,
        html_content=str_html_content)
    sg = SendGridAPIClient(str_api_key)
    response = sg.send(mail_message)
    print(response.status_code, response.body, response.headers)
