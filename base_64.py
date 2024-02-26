# Take the below hex string, decode it into bytes and then encode it into Base64.

import base64

encoded = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Decoded from hex into byte
into_byte = bytes.fromhex(encoded)

# Encoded into base64 string
into_base64 = base64.b64encode(into_byte)

print(into_byte)
print(into_base64)
