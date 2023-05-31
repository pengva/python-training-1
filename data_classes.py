from dataclasses import dataclass


@dataclass
class ReceiverData:
    email: str
    subject: str
    text: str

    def __init__(self, email: str, subject: str, text: str):
        self.email = email
        self.subject = subject
        self.text = text


@dataclass
class MailerArguments:
    email: str
    app_password: str
    csv_path: str

    def __init__(self, email: str, app_password: str, csv_path: str):
        self.email = email
        self.app_password = app_password
        self.csv_path = csv_path
