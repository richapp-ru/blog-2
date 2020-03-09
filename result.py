import os
import shutil
from helpers import sizePretty
from serialize_types import TYPES_LIST

class Result(object):

    RESULTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results")
    MAX_TYPE_LEN = max([len(item) for item in TYPES_LIST])
    MAX_TIME_LEN = 0
    MAX_SIZE_LEN = 0
    _serializeBenchmarks = []
    _deserializeBenchmarks = []

    @classmethod
    def _printLine(cls):
        print("+-{}-+-{}-+-{}-+".format(
            "-".ljust(cls.MAX_TYPE_LEN, "-"),
            "-".ljust(cls.MAX_TIME_LEN, "-"),
            "-".ljust(cls.MAX_SIZE_LEN, "-"),
        ))

    @classmethod
    def _printHeader(cls, title, fields):
        print("")
        print(title)
        cls._printLine()
        print("| {} | {} | {} |".format(
            fields[0].ljust(cls.MAX_TYPE_LEN),
            fields[1].ljust(cls.MAX_TIME_LEN),
            fields[2].ljust(cls.MAX_SIZE_LEN),
        ))
        cls._printLine()

    @classmethod
    def init(cls):
        shutil.rmtree(cls.RESULTS_DIR, ignore_errors=True)
        os.mkdir(cls.RESULTS_DIR)

    @classmethod
    def addSerializeBenchmark(cls, serializeType, time, size):
        formatedTime = "{:.6f}".format(time)
        formatedSize = sizePretty(size)
        cls._serializeBenchmarks.append({
            "type": serializeType,
            "time": time,
            "formatedTime": formatedTime,
            "size": size,
            "formatedSize": formatedSize,
        })
        if len(formatedTime) > cls.MAX_TIME_LEN:
            cls.MAX_TIME_LEN = len(formatedTime)
        if len(formatedSize) > cls.MAX_SIZE_LEN:
            cls.MAX_SIZE_LEN = len(formatedSize)

    @classmethod
    def addDeserializeBenchmark(cls, serializeType, time):
        formatedTime = "{:.6f}".format(time)
        cls._deserializeBenchmarks.append({
            "type": serializeType,
            "time": time,
            "formatedTime": formatedTime,
        })
        if len(formatedTime) > cls.MAX_TIME_LEN:
            cls.MAX_TIME_LEN = len(formatedTime)

    @classmethod
    def report(cls):
        cls._printHeader("Serialize report:", ["Type", "Time", "Size"])
        for bench in cls._serializeBenchmarks:
            print("| {} | {} | {} |".format(
                bench["type"].ljust(cls.MAX_TYPE_LEN),
                bench["formatedTime"].ljust(cls.MAX_TIME_LEN),
                bench["formatedSize"].ljust(cls.MAX_SIZE_LEN),
            ))
        cls._printLine()

        cls._printHeader("Deserialize report:", ["Type", "Time", ""])
        for bench in cls._deserializeBenchmarks:
            print("| {} | {} | {} |".format(
                bench["type"].ljust(cls.MAX_TYPE_LEN),
                bench["formatedTime"].ljust(cls.MAX_TIME_LEN),
                "".ljust(cls.MAX_SIZE_LEN),
            ))
        cls._printLine()
