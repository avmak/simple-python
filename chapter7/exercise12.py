import binaascii

gif = binascii.unhexlify(b'47494638396101000100800000000000ffffff21f9' + \
    b'0401000000002c000000000100010000020144003b')
print(gif)                                                                      # output: b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
len(gif)                                                                        # output: 42
