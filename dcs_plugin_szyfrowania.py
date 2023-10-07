import random

def losowy_klucz():
    return random.randint(0, 2 ** 128 - 1)

def losowy_klucz_prosty():
    return random.randint(0, 2 ** 10 - 1)

def info(zmienna = False):
    '''
    wyświetla informacje o programie
    :param zmienna: zmienia typ informacji dla True (dokładniejsze)
    :return: brak
    '''
    if zmienna == True:
        print("Nazwa: DCS Plugin Szyfrowania")
        print("Autor: Dawid Cisiński")
        print("Wersja:1.0")
        return
    else:
        return "DCS Plugin Szyfrowania v.1.0"

def szyfruj_tablice(tablica, klucz_szyfrowania):
    kod_szyfrowania = ""
    while klucz_szyfrowania > 0:
        kod_szyfrowania += chr(klucz_szyfrowania % 256)
        klucz_szyfrowania //= 256
    kod_szyfrowania = kod_szyfrowania.zfill(16)

    zaszyfrowana_tablica = []
    for element in tablica:
        zaszyfrowany_element = ""
        for i in range(len(element)):
            zaszyfrowany_znak = chr(ord(element[i]) ^ ord(kod_szyfrowania[i % 16]))
            zaszyfrowany_element += zaszyfrowany_znak
        zaszyfrowana_tablica.append(zaszyfrowany_element)

    return zaszyfrowana_tablica


def odszyfruj_tablice(tablica, klucz_szyfrowania):
    kod_szyfrowania = ""
    while klucz_szyfrowania > 0:
        kod_szyfrowania += chr(klucz_szyfrowania % 256)
        klucz_szyfrowania //= 256
    kod_szyfrowania = kod_szyfrowania.zfill(16)

    odszyfrowana_tablica = []
    for element in tablica:
        odszyfrowany_element = ""
        for i in range(len(element)):
            odszyfrowany_znak = chr(ord(element[i]) ^ ord(kod_szyfrowania[i % 16]))
            odszyfrowany_element += odszyfrowany_znak
        odszyfrowana_tablica.append(odszyfrowany_element)

    return odszyfrowana_tablica

def szyfruj_tablice_na_str(lista, klucz):
    tekst = ' '.join(lista)
    szyfr = ""
    for znak in tekst:
        kod = ord(znak)
        kod += klucz
        nowy_znak = chr(kod)
        szyfr += nowy_znak
    return szyfr


def odszyfruj_str_na_tablice(tekst, klucz):
    tekst_jawny = ""
    for znak in tekst:
        kod = ord(znak)
        kod -= klucz
        nowy_znak = chr(kod)
        tekst_jawny += nowy_znak

    str = tekst_jawny
    if "." in str:
        str = str.replace(".", "")
    str += " "
    tablica = []
    miejsce = 0
    for index, i in enumerate(str):
        if i == " ":
            tablica.append(str[miejsce:index])
            miejsce = index + 1
    return tablica

#Dawid Csisiński

