import configparser
import pytest
from email_lab.email_sendgrid import send_email


# @pytest.mark.skip
@pytest.mark.itest
def test_it_should_send_email():
    config = configparser.ConfigParser()
    print(config)
    # config.read(os.environ.get('CONF_SENDGRID')) # you could set the path to the config file via an env. var.
    config.read('./conf/sendgrid.conf')
    subject = "News you can use, maybe..."
    html_message = "<h2>Hi, here is your news for the day! Can you use news from <a href='https://bbc.com/'>BBC</a></h2><br />Have a great day!"
    send_email(
        config['email_sendgrid']['from_email'],
        config['email_sendgrid']['to_emails'],
        config['email_sendgrid']['api_key'],
        subject,
        html_message)
    assert 1 == 1
