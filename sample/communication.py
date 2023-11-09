# sample/communications.py

import smtplib  # creation of smtp client session and sending emails
import ssl  # TLSv1.3 security -- secure encryption
from email.mime.text import MIMEText  # email content building
from email.mime.multipart import MIMEMultipart  # email content building


def send_email(sender, api_key, receiver, message,
               display_language: str = "EN") -> bool:
    """
    Send an encrypted (TLSv1.3) email with the specified message.
    :param sender: the one initiating the contact
    :param api_key: the sender account's api key
    :param receiver: the recipient of the connection
    :param message: the content
    :param display_language: denoting the language to display the messages in
    -- Prepared messages available in english (EN - default) and hungarian (
    HU).
    :return: true if successful, false otherwise
    """

    # email was successfully sent flag
    successfully_sent = False

    # connection details -- SMTP server settings for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # TLS port for Gmail
    smtp_username = sender
    smtp_password = api_key

    # email sender and receiver
    sender_email = sender
    receiver_email = receiver

    # email subject field
    if display_language == "HU":
        subject = "[🎅🏽TitkosMikulás - 2023🤶🏼] - karácsonyi névhúzás🎁"
    else:
        subject = "[🎅🏽SecretSanta - 2023🤶🏼] - pairing results🎁"

    # Create a MIMEText object for the email content
    email_content = MIMEMultipart()
    email_content["From"] = sender_email
    email_content["To"] = receiver_email
    email_content["Subject"] = subject
    # Attach the message to the email
    email_content.attach(MIMEText(message, "html"))

    # Establish a TLSv1.3 secure connection
    context = ssl.create_default_context()
    context.minimum_version = ssl.TLSVersion.TLSv1_3

    try:
        # server.quit() is automatically issued when with exits
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Upgrade connection to secure TLSv1.3
            server.starttls(context=context)
            # Login to your email account
            server.login(smtp_username, smtp_password)
            # Send the email
            server.sendmail(sender_email, receiver_email,
                            email_content.as_string())
    except Exception as e:
        print("[ERROR] while sending the email: ", str(e))
    else:
        successfully_sent = True

    return successfully_sent


def craft_message(giver: str, recipient: str,
                  recipients_wish: str = None,
                  display_language: str = "EN") -> str:
    """
    Craft the displayed email message in html.
    :param giver: The one who gives the gift.
    :param recipient: The one who receives the gift.
    :param recipients_wish: The wish noted by the recipient.
    :param display_language: denoting the language to display the messages in
    -- Prepared messages available in english (EN - default) and hungarian (
    HU).
    :return: A properly formatted html message.
    """

    # do it yourself message for missing wish -- for both languages
    default_recipients_wish_en = ("This member did NOT specify any wish, so "
                                  "it's completely up to your imagination. "
                                  "Good luck!😉")
    default_recipients_wish_hu = ("Ez a személy NEM adott meg semmilyen "
                                  "kívánságot, ezért teljesen a képzeletedre"
                                  " van bízva. Sok szerencsét!😉")

    if display_language == "HU":
        if recipients_wish is None:
            recipients_wish = default_recipients_wish_hu
        else:
            recipients_wish = (f"Ne aggódj, ha nincs ötleted a tökéletes "
                               f"ajándékra. <strong>{recipient}</strong> volt "
                               f"olyan kedves, hogy megadjon egy "
                               f"kívánságlistát, amit akár útmutatóként is "
                               f"használhatsz. 😉 <br><br>A lista "
                               f"akövetkező:<br> "
                               f" {recipients_wish}")
    else:
        if recipients_wish is None:
            recipients_wish = default_recipients_wish_en
        else:
            recipients_wish = (f"Your are lucky, <strong>{recipient}</strong> "
                               f"provided you with the following wishing list "
                               f"which you could use as a guidance😉: <br><br>"
                               f"{recipients_wish}")

    if recipients_wish is None:
        if display_language == "HU":
            recipients_wish = default_recipients_wish_hu
        else:
            recipients_wish = default_recipients_wish_en

    # using various html tags for text formatting -- english version
    html_formatted_message_en = \
        f"""<html>
                <body>
                    <p>Hello <strong>{giver}</strong> ☺️<br><br>
                        You got to be this years secret santa 
                        for: ... 🥁...🥁...🥁...wait for it....
                        <h1>{recipient}</h1>
                    </p>
                    <p>
                        {recipients_wish}
                    </p>
                </body>
            </html>
        """

    # using various html tags for text formatting -- hungarian version
    html_formatted_message_hu = \
        f"""<html>
                <body>
                    <p>Szia <strong>{giver}</strong> ☺️<br><br>
                        Ebben az évben a karácsonyi húzás keretében a 
                        következő személyt húztad: ... 
                        🥁...🥁...🥁...várd ki a végét...
                        <h1>🎉🎉🎉{recipient}🎉🎉🎉</h1>
                    </p>
                    <p>
                        {recipients_wish}
                    </p>
                </body>
            </html>
        """

    # decide for the correct language
    if display_language == "HU":
        return html_formatted_message_hu
    else:
        return html_formatted_message_en


def send_verification_email(sender: str, api_key: str, receiver: str,
                            message: str) -> bool:
    """
    Send yourself the pairings as an encrypted (TLSv1.3) email for
    verification.
    :param sender: both the sender and the recevier in this case
    :param api_key: the sender account's api key
    :param receiver: the recipient of the connection
    :param message: the pairings in a string format
    :return: true if successful, false otherwise
    """

    # email was successfully sent flag
    successfully_sent = False

    # connection details -- SMTP server settings for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # TLS port for Gmail
    smtp_username = sender
    smtp_password = api_key

    # email sender and receiver
    sender_email = sender

    # email subject field
    subject = "[🎅🏽SecretSanta - 2023🤶🏼] - pairing results🎁"

    # Create a MIMEText object for the email content
    email_content = MIMEMultipart()
    email_content["From"] = sender_email
    email_content["To"] = sender_email
    email_content["Subject"] = subject

    # Attach the message to the email
    email_content.attach(MIMEText(message, "plain"))

    # Establish a TLSv1.3 secure connection
    context = ssl.create_default_context()
    context.minimum_version = ssl.TLSVersion.TLSv1_3

    try:
        # server.quit() is automatically issued when with exits
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Upgrade connection to secure TLSv1.3
            server.starttls(context=context)
            # Login to your email account
            server.login(smtp_username, smtp_password)
            # Send the email
            server.sendmail(sender_email, receiver,
                            email_content.as_string())
    except Exception as e:
        print("[ERROR] while sending the email: ", str(e))
    else:
        successfully_sent = True

    return successfully_sent
