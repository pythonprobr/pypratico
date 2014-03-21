import urllib

pag = urllib.urlopen('http://www5.usp.br')

txt = pag.read()

for lin in txt.split('\n'):
    if 'curso' in lin:
        print lin


