import os
from time import time
import json
import pickle
import ujson
import progressbar

from result import Result
from helpers import sizePretty
from serialize_types import SerializeTypes
from csv_format import csvSerialize, csvDeserialize, csvDictDeserialize
from protobuf_format import protobufDeserialize

deserializeFunctions = {}
deserializeFunctions[SerializeTypes.json] = json.loads
deserializeFunctions[SerializeTypes.ujson] = ujson.loads
deserializeFunctions[SerializeTypes.csv] = csvDeserialize
deserializeFunctions[SerializeTypes.csvDict] = csvDictDeserialize
deserializeFunctions[SerializeTypes.protobuf] = protobufDeserialize
deserializeFunctions[SerializeTypes.pickle] = pickle.loads


def deserializeBenchmark(iterations, serializeType, serializedData):
    fn = deserializeFunctions[serializeType]
    result = []
    print("[{}] Start deserialize benchmark".format(serializeType))
    for i in progressbar.progressbar(range(iterations)):
        start = time()
        data = fn(serializedData)
        result.append(time() - start)

    Result.addDeserializeBenchmark(
        serializeType,
        result
    )
    with open(os.path.join(Result.RESULTS_DIR, "deserialized-{}.csv".format(serializeType)), "w") as fstream:
        fstream.write(csvSerialize(data))

    return data
