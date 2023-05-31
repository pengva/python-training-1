from data_classes import MailerArguments
import argparse


def readArguments():
    parser = argparse.ArgumentParser(
        description="Mailer"
    )

    parser.add_argument('-email', metavar='e', nargs='?',
                        help="Email to send from message")
    parser.add_argument('-app_password', metavar="p", nargs="?",
                        help="Gmail app password")
    parser.add_argument('-csv', metavar='c', nargs='?',
                        help="Receivers data .csv path")

    args = parser.parse_args()

    email = args.email
    password = args.app_password
    csv_path = args.csv

    if email is None:
        print("-email is required")
        quit(1)

    if password is None:
        print("-app_password is required")
        quit(1)

    if csv_path is None:
        print("-csv is required")
        quit(1)

    return MailerArguments(email=email, app_password=password, csv_path=csv_path)
