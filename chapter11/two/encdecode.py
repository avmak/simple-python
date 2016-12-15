def str_to_bytes(bos):
    if isinstance(bos, str):
        value = bos.encode('utf-8')
    else:
        value = bos
    return value


def bytes_to_str(bos):
    if isinstance(bos, bytes):
        value = bos.decode('utf-8')
    else:
        value = bos
    return value
