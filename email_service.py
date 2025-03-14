from aiosmtplib import send
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, EMAIL_FROM, SMTP_PASSWORD, SMTP_USER


async def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_FROM
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    await send(
        msg,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASSWORD,
        use_tls=False,
        start_tls=True,
    )
