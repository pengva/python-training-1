from mailer import Mailer, Message

from arguments_reader import readArguments
from csv_reader import readCsv


def createMailer(email: str, app_password: str):
    try:
        return Mailer(host='smtp.gmail.com',
                      port=465,
                      use_ssl=True,
                      use_tls=False,
                      usr=email,
                      pwd=app_password)
    except:
        print("Mailer initialization error. Please verify provided email and app_password")
        quit(1)


arguments = readArguments()
mail = createMailer(email=arguments.email, app_password=arguments.app_password)
receivers = readCsv(arguments.csv_path)

for receiver in receivers:
    try:
        print("Sending message to " + receiver.email)
        message = Message(From=arguments.email, To=receiver.email, charset="utf-8")
        message.Subject = receiver.subject
        message.Body = receiver.text
        mail.send(message)
        print("Sent message successfully")
    except:
        print(
            "Error occurred during sending message to " + receiver.email + '. Please verify provided email, '
                                                                           'app_password and csv data')
