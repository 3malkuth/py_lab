import sys
import configparser
import email_sendgrid


def main():
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    subject = "News you can use, maybe..."
    html_message = "<h2>Hi, here is your news for the day! Can you use news from <a href='https://bbc.com/'>BBC</a></h2><br />Have a great day!"
    email_sendgrid.send_email(
        config['email_sendgrid']['from_email'],
        config['email_sendgrid']['to_emails'],
        config['email_sendgrid']['api_key'],
        subject,
        html_message)


if __name__ == '__main__':
    main()
