from plik_def import *

path = 'C://Users//kamusial//Desktop//rolling_stones.txt'

text = zapisDanychzPliku(path)
print(type(text))
tekst = przygotowanie(text)
print(type(text))

print('liczba unikalnych słów to ', ileSlow(tekst))
print(ileRazy(text))

