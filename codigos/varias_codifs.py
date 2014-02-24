# Fonte:
# https://mail.python.org/pipermail/python-list/2012-June/624991.html

import sys

class Writer:
    def __init__(self, output):
        self.output = output
        self.encoding = output.encoding
    def write(self, string):
        self.output.buffer.write(string.encode(self.encoding))
    def set_encoding(self, encoding):
        self.output.buffer.flush()
        self.encoding = encoding
    def flush(self):
    	self.output.flush()

sys.stdout = Writer(sys.stdout)

initial_encoding = sys.stdout.encoding

text = '%10s --> 世界へ、こんにちは！'
sys.stdout.set_encoding('utf-8')
print (text % 'utf-8')
sys.stdout.set_encoding('sjis')
print (text % 'sjis')
sys.stdout.set_encoding('euc-jp')
print (text % 'euc-jp')
sys.stdout.set_encoding('iso2022-jp')
print (text % 'iso2022-jp')

sys.stdout.set_encoding(initial_encoding)
