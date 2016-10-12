import binaascii

gif = binascii.unhexlify(b'47494638396101000100800000000000ffffff21f9' + \
    b'0401000000002c000000000100010000020144003b')
valid_gif = b'GIF98a'

if gif[0:6] == valid_gif:
    width, height = struct.unpack('>HH', gif[6:10])
	print('Valid gif, width', width, 'height', height)                             # output: Valid gif, width 256 height 256
