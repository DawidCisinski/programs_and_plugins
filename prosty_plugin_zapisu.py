import os
#Config#
SPR_TXT_AUTO = "przykladowy_plik.txt" #odgórna nazwa pliku zapisu/odczytu
SPR_AUTO = False #automatyczne uzupełnianie
#Config#

def czyszczenie_ekranu():
    '''czyści ekran'''
    os.system("cls")
    i = 10
    for i in range(1, 10):
        pass

def info(zmienna = False):
    '''
    wyświetla informacje o programie
    :param zmienna: zmienia typ informacji dla True (dokładniejsze)
    :return: brak
    '''
    if zmienna == True:
        print("Prosty plugin zapisu")
        print("Autor: Dawid Cisiński")
        print("Wersja:1.1")
        return
    else:
        return "Zapis pro v.1.1"

def spr_txt():
    global SPR_TXT_AUTO
    global SPR_AUTO
    if SPR_TXT_AUTO != "przykladowy_plik.txt":
        return SPR_TXT_AUTO
    else:
        czyszczenie_ekranu()
        plik = input("Wybierz nazwę dla pliku: ")
        if ".txt" not in plik:
            plik = plik + ".txt"
            return plik
        else:
            return plik

def wczytaj():
    """
    wczytuje plik
    :return: zwraca tablice
    """
    global SPR_AUTO
    if SPR_AUTO == True:
        plik = spr_txt()
        if os.path.exists(plik):
            with open(plik, "r") as plik:
                lista = eval(plik.read())
            czyszczenie_ekranu()
            return lista
    else:
        while True:
            plik = spr_txt()
            if os.path.exists(plik):
                with open(plik, "r") as plik:
                    lista = eval(plik.read())
                return lista
            else:
                if input("Podany plik nie istnieje czy chcesz wczytać pustą tablice? (T/N): ").lower() == "t":
                    czyszczenie_ekranu()
                    print("odczyt zakończony sukcesem")
                    return []
        czyszczenie_ekranu()
        print("odczyt zakończony sukcesem")
        return

def zapisz(lista):
    """
    zapisuje do wcześniej utworzonego pliku algo go tworzy
    :param lista: tablica do zapisu
    :return: brak
    """
    global SPR_AUTO
    if SPR_AUTO == True:
        plik = SPR_TXT_AUTO
        with open(plik, "w") as plik: # uzyj zmiennej plik zamiast SPR_AUTO
            plik.write(str(lista))
            czyszczenie_ekranu()
            print("zapis pomyślny")
            return
    else:
        while True:
            plik = spr_txt()
            if os.path.exists(plik):
                with open(plik, "w") as plik:
                    plik.write(str(lista))
                    break
            else:
                czyszczenie_ekranu()
                if input("Podany plik nie istnieje czy chcesz go stworzyć? (T/N): ").lower() == "t":
                    with open(plik, "w") as plik:
                        plik.write(str(lista))
                        break
                else:
                    print("wpisz inną nazwe")
                    pass
        czyszczenie_ekranu()
        print("zapis pomyślny")

def zapisz_jako(lista):
    """
    zapisuje do nowego pliku albo nadpisuje
    :param lista: tablica do zapisu
    :return: brak
    """
    global SPR_AUTO
    if SPR_AUTO == True:
        plik = SPR_TXT_AUTO
        with open(plik, "w") as plik:
            plik.write(str(lista))
            czyszczenie_ekranu()
            print("zapis pomyślny")
            return
    else:
        while True:
            plik = spr_txt()
            if not os.path.exists(plik):
                with open(plik, "w") as plik:
                    plik.write(str(lista))
                    break
            else:
                czyszczenie_ekranu()
                if input("Podany plik istnieje czy chcesz go nadpisać? (T/N): ").lower() == "t":
                    with open(plik, "w") as plik:
                        plik.write(str(lista))
                        break
                else:
                    print("wpisz inną nazwe")
                    pass
        czyszczenie_ekranu()
        print("zapis pomyślny")

# Autor: Dawid Cisiński
