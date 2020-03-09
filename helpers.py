
sizeMetrics = [
    "B",
    "KB",
    "MB",
    "GB",
    "TB",
]


def sizePretty(size, index=0):
    if size == 0:
        return "0"

    if index == len(sizeMetrics) - 1 or float(size) / float(1024) < 1:
        return "{:.2f} {}".format(size, sizeMetrics[index])
    else:
        return sizePretty(float(size) / float(1024), index+1)
