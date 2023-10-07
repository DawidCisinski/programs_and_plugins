import json
import os


class Budowniczy:
    def __init__(self, rozszerzenie="xyz", nazwa_folderu="folder_zapisu", nazwa_pliku="xyz_plik", auto=False):
        self.auto = auto
        self.rozszerzenie = "." + rozszerzenie
        self.nazwa_folderu = nazwa_folderu
        self.katalog_domowy = os.path.expanduser("~")
        self.sciezka_folderu = os.path.join(self.katalog_domowy, self.nazwa_folderu)
        if not os.path.exists(self.sciezka_folderu):
            os.mkdir(self.sciezka_folderu)
            print(f"Utworzono folder {self.sciezka_folderu}")
        self.auto_plik = self.sciezka_folderu + "\\" + nazwa_pliku + self.rozszerzenie

    def spr_txt(self):
        plik = input("Wpisz nazwe Projektu: ")
        plik = plik.lower()
        if self.rozszerzenie in plik:
            return plik
        else:
            plik = self.sciezka_folderu + "\\" + plik + self.rozszerzenie
            print(plik)
            return plik

    def zapisz(self, lista):
        """
        zapisuje do wcześniej utworzonego pliku algo go tworzy
        :param lista: tablica do zapisu
        :return: brak
        """
        if self.auto == True:
            plik = self.auto_plik
            with open(plik, "w", encoding="utf-8") as file:
                json.dump(lista, file)
        else:
            while True:
                plik = self.spr_txt()
                if os.path.exists(plik):
                    with open(plik, "w", encoding="utf-8") as file:
                        json.dump(lista, file)
                    break
                else:
                    if input("Podany plik nie istnieje czy chcesz go stworzyć? (T/N): ").lower() == "t":
                        with open(plik, "w", encoding="utf-8") as file:
                            json.dump(lista, file)
                        break
                    else:
                        print("wpisz inną nazwe")
                        pass
        os.system("cls")
        return True

    def zapisz_jako(self, lista):
        """
        zapisuje do nowego pliku albo nadpisuje
        :param lista: tablica do zapisu
        :return: brak
        """
        if self.auto == True:
            plik = self.auto_plik
            with open(plik, "w", encoding="utf-8") as file:
                json.dump(lista, file)
                os.system("cls")
        else:
            while True:
                plik = self.spr_txt()
                if not os.path.exists(plik):
                    with open(plik, "w", encoding="utf-8") as file:
                        json.dump(lista, file)
                    break
                else:
                    if input("Podany plik istnieje czy chcesz go nadpisać? (T/N): ").lower() == "t":
                        with open(plik, "w", encoding="utf-8") as file:
                            json.dump(lista, file)
                        break
                    else:
                        print("wpisz inną nazwe")
                        pass
        os.system("cls")
        return True

    def wczytaj(self):
        """
        wczytuje plik
        :return: zwraca tablice
        """
        if self.auto == True:
            plik = self.auto_plik
            if os.path.exists(plik):
                with open(plik, "r", encoding="utf-8") as file:
                    lista = json.load(file)
                os.system("cls")
                return lista
        else:
            while True:
                plik = self.spr_txt()
                if os.path.exists(plik):
                    with open(plik, "r", encoding="utf-8") as file:
                        lista = json.load(file)
                    os.system("cls")
                    return lista
                else:
                    if input("Podany plik nie istnieje czy chcesz wczytać pustą tablice? (T/N): ").lower() == "t":
                        os.system("cls")
                        print("odczyt zakończony sukcesem")
                        return []

    def zawartosc_folderu(self, zmienna=False):
        """

        :param zmienna: True zwraca tablice plików, False zwraca liste print()
        :return: lista plików danego folderu
        """
        dane = self.sciezka_folderu
        pliki = os.listdir(dane)
        if zmienna == True:
            return pliki
        else:
            print(*pliki, sep=' ')
            return ""

    def usun_plik(self):
        if self.auto == True:
            if os.path.isfile(self.auto_plik):
                os.remove(self.auto_plik)
        else:
            dane = self.sciezka_folderu
            pliki = os.listdir(dane)
            print(*pliki, sep=' ')
            wybor = input("wybierz nazwe: ")
            if wybor in pliki:
                wybor2 = self.sciezka_folderu + "\\" + wybor
                os.remove(wybor2)
            elif wybor + self.rozszerzenie in pliki:
                wybor = wybor + self.rozszerzenie
                wybor2 = self.sciezka_folderu + "\\" + wybor
                os.remove(wybor2)
        os.system("cls")
        return True

    def info(self, zmienna=False):
        '''
        wyświetla informacje o programie
        :param zmienna: zmienia typ informacji dla True (dokładniejsze)
        :return: zwraca nazwe programu
        '''
        if zmienna == True:
            os.system("cls")
            print("Nazwa: DCS Plugin zapisu")
            print("Autor: Dawid Cisiński")
            print("Wersja:2.0")
        else:
            os.system("cls")
            return "DCS Plugin zapisu v.2.0"
# Autor Dawid Cisiński

#lista = ["xyz"]
#lista = dcs_plugin_zapisu.proste_menu_zapisu(lista)

def proste_menu_zapisu(lista, rozszerzenie="opensave", folder="ProjektyOpenSave"):
    os.system("cls")
    opacja_zapisu = Budowniczy(rozszerzenie, folder)
    koniec = False
    while True:
        print("# # # # # # # #")
        print("#  __Menu__   #")
        print("#  1.Zapisz   #")
        print("#  2.Wczytaj  #")
        print("#  3.Wyjdź    #")
        print("# # # # # # # #")
        print("")
        wybor = input("Wybieram: ")
        if wybor == "1":
            os.system("cls")
            opacja_zapisu.zapisz(lista)
            print("Zapis Pomyślny")
        elif wybor == "2":
            os.system("cls")
            koniec = opacja_zapisu.wczytaj()
            print("Odczyt Pomyślny")
        else:
            os.system("cls")
            break
    return koniec
# Autor Dawid Cisiński
