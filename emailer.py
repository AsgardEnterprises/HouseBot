import smtplib
import credentials
import config


def send_notification_emails(text):
    """
    Sends notification emails to the addresses specified in config.house_member_email_addresses.
    Aborts if no recipient emails are found.
    :param text:
    :return:
    """
    recipients = []
    house_member_details = config.house_member_details
    for house_member in house_member_details:
        recipients.append(house_member["email_address"])

    if len(recipients) == 0:
        print("No email addresses specified. No emails will be sent.")
    else:
        send_email(recipients, text)


def send_email(recipients, text):
    """
    Sends an email using the gmail account whose credentials are specified in credentials.json
    :param recipients:
    :param text:
    :return:
    """
    gmail_user = credentials.gmail_address
    gmail_pwd = credentials.gmail_password
    FROM = credentials.gmail_address
    TO = recipients  # must be a list
    SUBJECT = "HouseBot Notification - new properties matching your description found!"
    TEXT = text

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except smtplib.SMTPAuthenticationError as e:
        print "Failed to send email due to an authentication error."
        print "SMTPAuthenticationError: " + str(e.smtp_error)
    except Exception as e:
        print "Failed to send mail"
        print str(e.args)
