def zapisDanychzPliku(path):
    with open(path, 'r') as plik:
        content = plik.read()
    content = content.split()
    return content


def przygotowanie(text):
    for i in range(len(text)):
        text[i] = text[i].lower()
        text[i] = text[i].replace('.','')
    return text


def ileRazy(text):
    slownik = {}
    for i in range (len(text)):
        for j in text[i]:
            if j in slownik:
                slownik[j] += 1
            else:
                slownik[j] = 1
    for a, b in slownik.items():
        print(f'slowo {a} powtarza się {b} razy')


def ileSlow(text):
    tekst = set(text)
    return len(set(text))