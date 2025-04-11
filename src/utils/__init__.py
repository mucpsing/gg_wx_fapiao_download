import hashlib, time


def str2md5(inputStr: str = None) -> str:
    if not inputStr:
        inputStr = str(time.time())

    obj = hashlib.md5()

    obj.update(inputStr.encode("utf-8"))

    return obj.hexdigest()
