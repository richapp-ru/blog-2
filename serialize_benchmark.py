import os
from time import time
import json
import pickle
import ujson
import progressbar

from result import Result
from serialize_types import SerializeTypes
from csv_format import csvSerialize, csvDictSerialize
from protobuf_format import protobufSerialize

serializeFunctions = {}
serializeFunctions[SerializeTypes.json] = json.dumps
serializeFunctions[SerializeTypes.ujson] = ujson.dumps
serializeFunctions[SerializeTypes.csv] = csvSerialize
serializeFunctions[SerializeTypes.csvDict] = csvDictSerialize
serializeFunctions[SerializeTypes.protobuf] = protobufSerialize
serializeFunctions[SerializeTypes.pickle] = pickle.dumps


def serializeBenchmark(iterations, serializeType, data):
    fn = serializeFunctions[serializeType]
    totalTime = float(0)
    print("[{}] Start serialize bechmark".format(serializeType))
    for i in progressbar.progressbar(range(iterations)):
        start = time()
        serializedData = fn(data)
        totalTime += time() - start

    Result.addSerializeBenchmark(
        serializeType,
        totalTime / float(iterations),
        len(serializedData)
    )

    flags = "w"
    if type(serializedData) == bytes:
        flags = "wb"
    with open(os.path.join(Result.RESULTS_DIR, "serialized-{}".format(serializeType)), flags) as fstream:
        fstream.write(serializedData)

    return serializedData
