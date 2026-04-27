#!/usr/bin/env python3
"""Send AI Newsletter HTML via Gmail SMTP. Usage: python send_email.py <html_file> <date_label>"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

FROM_EMAIL = "leisurewilliam@gmail.com"
TO_EMAIL = "lema@glprop.com"


def send(html_path: str, date_label: str) -> None:
    app_password = os.environ.get("GMAIL_APP_PASSWORD", "")
    if not app_password:
        raise EnvironmentError("GMAIL_APP_PASSWORD environment variable not set")

    html = Path(html_path).read_text(encoding="utf-8")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"AI 日报 · {date_label}"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg.attach(MIMEText(html, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(FROM_EMAIL, app_password)
        server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
        print(f"Email sent successfully to {TO_EMAIL}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python send_email.py <html_file> <date_label>")
        sys.exit(1)
    send(sys.argv[1], sys.argv[2])
