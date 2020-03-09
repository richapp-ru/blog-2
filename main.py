#!/usr/bin/env python3
import os
import sys
import argparse

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.append(CUR_DIR)
from result import Result
from serialize_types import TYPES_LIST
from csv_format import csvSerialize
from generate_data import generateData
from serialize_benchmark import serializeBenchmark
from deserialize_benchmark import deserializeBenchmark

def main():
    parser = argparse.ArgumentParser("")

    parser.add_argument("--iterations", dest="iterations", type=int, default=100)
    parser.add_argument("--data-size", dest="dataSize", type=int, required=True)

    args = parser.parse_args()
    data = generateData(args.dataSize)

    Result.init()

    for serializeType in TYPES_LIST:
        serializedData = serializeBenchmark(args.iterations, serializeType, data)
        deserializedData = deserializeBenchmark(args.iterations, serializeType, serializedData)

    Result.report()


if __name__ == "__main__":
    main()
