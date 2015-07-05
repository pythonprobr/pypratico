import os
import base64

octetos = os.urandom(9)  # 9 * 8 = 72 bits
cars = base64.b64encode(octetos)  # 72 bits --> 12 cars
print(cars.decode('ascii'))  # bytes ASCII --> str Unicode
