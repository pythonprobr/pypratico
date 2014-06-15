amostra = ['B', 'Ã', 'ç', '\u6c23', '\U0001f004']

fmt = '{car:2}\tU+{cp:04X}\t {utf8_hex:8}\t{utf8_bits:35}\t{utf16_hex:8}'

def bitstr(octetos):
    return ' '.join(format(byte, '08b') for byte in octetos)

def hexstr(octetos):
    return ' '.join(format(byte, '02x') for byte in octetos)

for car in amostra:
    utf8 = car.encode('utf8')
    utf16 = car.encode('utf-16_be')
    print(fmt.format(car=car, cp=ord(car),
          utf8_hex=hexstr(utf8), utf8_bits=bitstr(utf8),
          utf16_hex=hexstr(utf16), utf16_bits=bitstr(utf16),
          ))
