from protobuf_format.transaction_pb2 import Data, Transaction

typeToProto = {
    "перевод": "transfer",
    "снятие": "withdraw",
    "пополнение": "fillup",
}
typeFromProto = {v: k for k, v in typeToProto.items()}


def protobufSerialize(data):
    protoData = Data()
    for item in data:
        protoData.transactions.append(Transaction(
            id=item["id"],
            type=typeToProto[item["type"]],
            amount=item["amount"],
            time=item["time"],
            message=item["message"]
        ))
    return protoData.SerializeToString()

def protobufDeserialize(serializedData):
    data = []

    protoData = Data()
    protoData.ParseFromString(serializedData)
    for transaction in protoData.transactions:
        data.append({
            "id": transaction.id,
            "type": typeFromProto[Transaction.Type.Name(transaction.type)],
            "amount": transaction.amount,
            "time": transaction.time,
            "message": transaction.message,
        })
    return data
