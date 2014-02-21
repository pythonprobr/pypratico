s = 'maçã'
print(len(s), s)
b_cp1252 = s.encode('cp1252')
print(type(b_cp1252))
b_utf8 = s.encode('utf8')
print('cp1252 (%s):' % len(b_cp1252), b_cp1252)
print('utf8 (%s):' % len(b_utf8), b_utf8)

s2 = b'ma\xe7\xe3'
print(s2, 'decode cp1252-->', s2.decode('cp1252'))