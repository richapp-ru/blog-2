import io
import csv


def csvSerialize(data):
    stream = io.StringIO()
    writer = csv.writer(stream)
    writer.writerow(["id", "type", "amount", "time", "message"])
    for item in data:
        writer.writerow([
            item["id"],
            item["type"],
            item["amount"],
            item["time"],
            item["message"],
        ])
    return stream.getvalue()


def csvDeserialize(serializedData):
    stream = io.StringIO(serializedData)
    reader = csv.reader(stream)
    next(reader)

    result = []
    for item in reader:
        result.append({
            "id": int(item[0]),
            "type": item[1],
            "amount": int(item[2]),
            "time": float(item[3]),
            "message": item[4]
        })
    return result


def csvDictSerialize(data):
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=["id", "type", "amount", "time", "message"])
    writer.writeheader()
    for item in data:
        writer.writerow(item)
    return stream.getvalue()


def csvDictDeserialize(serializedData):
    stream = io.StringIO(serializedData)
    reader = csv.DictReader(stream)

    result = []
    for item in reader:
        item["id"] = int(item["id"])
        item["amount"] = int(item["amount"])
        item["time"] = float(item["time"])
        result.append(item)
    return result
