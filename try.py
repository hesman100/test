from hexbytes import HexBytes

data = b'1\xd9\xec~8U\xae\xba7\xfd\x92\xaa\x169\x84^p\xb3`\xa6\x0fw\xf1.\xffS\x04)\xef\x8c\xfc\xba'

#  hex_data = HexBytes(data.hex())
hex_data = data.hex()

print(hex_data)  
