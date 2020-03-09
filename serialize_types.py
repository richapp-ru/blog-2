

class SerializeTypes(object):
    json = "json"
    ujson = "ujson"
    csv = "csv"
    csvDict = "csvDict"
    protobuf = "protobuf"
    pickle = "pickle"


TYPES_LIST = [
    SerializeTypes.json,
    SerializeTypes.ujson,
    SerializeTypes.csv,
    SerializeTypes.csvDict,
    SerializeTypes.protobuf,
    SerializeTypes.pickle
]
