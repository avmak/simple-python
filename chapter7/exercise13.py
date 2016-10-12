import binaascii

gif = binascii.unhexlify(b'47494638396101000100800000000000ffffff21f9' + \
    b'0401000000002c000000000100010000020144003b')

if gif[0:6] == b'GIF89a':
    print('gif is GIF-file')                                                    # output: gif is GIF-file
