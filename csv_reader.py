import csv

import data_classes


def readCsv(path: str):
    receivers = []

    try:

        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                receivers.append(
                    data_classes.ReceiverData(email=row['email'], subject=row['subject'], text=row['text']))

    except:
        print("Error reading csv file, please validate " + path + " file")
        quit(1)

    return receivers
