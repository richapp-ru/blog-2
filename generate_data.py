from time import time
from random import choice as randchoice
from random import randrange

START_ID = 10000000
TYPES = ["перевод", "снятие", "пополнение"]
START_AMOUNT = 3000
END_AMOUNT = 1000000
STEP = 1000


def generateData(size, startId=START_ID):
    data = []
    for i in range(size):
        data.append({
            "id": START_ID + i,
            "type": randchoice(TYPES),
            "amount": randrange(START_AMOUNT, END_AMOUNT, STEP),
            "time": time(),
            "message": "Transaction #{}".format(i)
        })
    return data
