import os
import base64

octets = os.urandom(9)  # 9 * 8 = 72 bits
chars = base64.b64encode(octets)  # 72 bits --> 12 chars
print(chars)
