import os
import shutil
import statistics
from helpers import sizePretty
from serialize_types import TYPES_LIST

class Result(object):

    RESULTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results")
    MAX_TYPE_LEN = max([len(item) for item in TYPES_LIST])
    MAX_TIME_LEN = 11
    MAX_SIZE_LEN = 0
    PERCENTAGE = 10
    _serializeBenchmarks = []
    _deserializeBenchmarks = []

    @classmethod
    def _printLine(cls):
        print("+-{}-+-{}-+-{}-+-{}-+".format(
            "-".ljust(cls.MAX_TYPE_LEN, "-"),
            "-".ljust(cls.MAX_TIME_LEN, "-"),
            "-".ljust(cls.MAX_SIZE_LEN, "-"),
            "-".ljust(cls.PERCENTAGE, "-"),
        ))

    @classmethod
    def _printHeader(cls, title, fields):
        print("")
        print(title)
        cls._printLine()
        print("| {} | {} | {} | {} |".format(
            fields[0].ljust(cls.MAX_TYPE_LEN),
            fields[1].ljust(cls.MAX_TIME_LEN),
            fields[2].ljust(cls.MAX_SIZE_LEN),
            fields[3].ljust(cls.PERCENTAGE)
        ))
        cls._printLine()

    @classmethod
    def init(cls):
        shutil.rmtree(cls.RESULTS_DIR, ignore_errors=True)
        os.mkdir(cls.RESULTS_DIR)

    @classmethod
    def addSerializeBenchmark(cls, serializeType, result, size):
        medianTime = statistics.median_low(result)
        cls._serializeBenchmarks.append({
            "type": serializeType,
            "medianTime": medianTime,
            "formatedMedianTime": "{:.6f}".format(medianTime),
            "size": size,
            "formatedSize": sizePretty(size),
        })

    @classmethod
    def addDeserializeBenchmark(cls, serializeType, result):
        medianTime = statistics.median_low(result)
        cls._deserializeBenchmarks.append({
            "type": serializeType,
            "medianTime": medianTime,
            "formatedMedianTime": "{:.6f}".format(medianTime),
        })

    @classmethod
    def report(cls):
        cls.minSerializeTime = cls._serializeBenchmarks[0]["medianTime"]
        for item in cls._serializeBenchmarks:
            if len(item["formatedMedianTime"]) > cls.MAX_TIME_LEN:
                cls.MAX_TIME_LEN = len(item["formatedMedianTime"])
            if len(item["formatedSize"]) > cls.MAX_SIZE_LEN:
                cls.MAX_SIZE_LEN = len(item["formatedSize"])
            if item["medianTime"] < cls.minSerializeTime:
                cls.minSerializeTime = item["medianTime"]

        cls.minDeserializeTime = cls._deserializeBenchmarks[0]["medianTime"]
        for item in cls._deserializeBenchmarks:
            if len(item["formatedMedianTime"]) > cls.MAX_TIME_LEN:
                cls.MAX_TIME_LEN = len(item["formatedMedianTime"])
            if item["medianTime"] < cls.minDeserializeTime:
                cls.minDeserializeTime = item["medianTime"]

        cls._printHeader("Serialize report:", ["Type", "Median Time", "Size", "Percentage"])
        for bench in cls._serializeBenchmarks:
            bench["percentage"] = str(int(bench["medianTime"] / cls.minSerializeTime * 100)) + "%"
            print("| {} | {} | {} | {} |".format(
                bench["type"].ljust(cls.MAX_TYPE_LEN),
                bench["formatedMedianTime"].ljust(cls.MAX_TIME_LEN),
                bench["formatedSize"].ljust(cls.MAX_SIZE_LEN),
                bench["percentage"].ljust(cls.PERCENTAGE),
            ))
        cls._printLine()

        cls._printHeader("Deserialize report:", ["Type", "Median Time", "", "Percentage"])
        for bench in cls._deserializeBenchmarks:
            bench["percentage"] = str(int(bench["medianTime"] / cls.minDeserializeTime * 100)) + "%"
            print("| {} | {} | {} | {} |".format(
                bench["type"].ljust(cls.MAX_TYPE_LEN),
                bench["formatedMedianTime"].ljust(cls.MAX_TIME_LEN),
                "".ljust(cls.MAX_SIZE_LEN),
                bench["percentage"].ljust(cls.PERCENTAGE),
            ))
        cls._printLine()
