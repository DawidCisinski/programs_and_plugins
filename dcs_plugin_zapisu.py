import os
#np_zapis = dcs_plugin_zapisu.budowniczy()
#lista = ["xyz"]
#np_zapis.zapisz(lista)
class budowniczy:
    def __init__(self,rozszerzenie = "xyz", nazwa_folderu = "folder_zapisu", nazwa_pliku = "xyz_plik", auto = False):
        self.auto = auto
        self.rozszerzenie = "." + rozszerzenie + ".txt"
        self.nazwa_folderu = nazwa_folderu
        self.katalog_domowy = os.path.expanduser("~")
        self.sciezka_folderu = os.path.join(self.katalog_domowy, self.nazwa_folderu)
        if not os.path.exists(self.sciezka_folderu):
            os.mkdir(self.sciezka_folderu)
            print(f"Utworzono folder {self.sciezka_folderu}")
        self.auto_plik = self.sciezka_folderu + "\\" + nazwa_pliku + self.rozszerzenie

    def spr_txt(self):
        plik = input("Wpisz nazwe Projektu: ")
        if self.rozszerzenie in plik:
            return plik
        else:
            plik = self.sciezka_folderu + "\\" + plik + self.rozszerzenie
            print(plik)
            return plik

    def czyszczenie_ekranu(self):
        os.system("cls")
        print("operacja powiodła się!")
        input("wciśnij dowolny klawisz... ")

    def zapisz(self, lista):
        """
        zapisuje do wcześniej utworzonego pliku algo go tworzy
        :param lista: tablica do zapisu
        :return: brak
        """
        if self.auto == True:
            plik = self.auto_plik
            with open(plik, "w") as plik:
                plik.write(str(lista))
                self.czyszczenie_ekranu()
                return
        else:
            while True:
                plik = self.spr_txt()
                if os.path.exists(plik):
                    with open(plik, "w") as plik:
                        plik.write(str(lista))
                        break
                else:
                    if input("Podany plik nie istnieje czy chcesz go stworzyć? (T/N): ").lower() == "t":
                        with open(plik, "w") as plik:
                            plik.write(str(lista))
                            break
                    else:
                        print("wpisz inną nazwe")
                        pass
            self.czyszczenie_ekranu()

    def zapisz_jako(self, lista):
        """
        zapisuje do nowego pliku albo nadpisuje
        :param lista: tablica do zapisu
        :return: brak
        """
        if self.auto == True:
            plik = self.auto_plik
            with open(plik, "w") as plik:
                plik.write(str(lista))
                self.czyszczenie_ekranu()
                return
        else:
            while True:
                plik = self.spr_txt()
                if not os.path.exists(plik):
                    with open(plik, "w") as plik:
                        plik.write(str(lista))
                        break
                else:
                    if input("Podany plik istnieje czy chcesz go nadpisać? (T/N): ").lower() == "t":
                        with open(plik, "w") as plik:
                            plik.write(str(lista))
                            break
                    else:
                        print("wpisz inną nazwe")
                        pass
            self.czyszczenie_ekranu()

    def wczytaj(self):
        """
        wczytuje plik
        :return: zwraca tablice
        """
        if self.auto == True:
            plik = self.auto_plik
            if os.path.exists(plik):
                with open(plik, "r") as plik:
                    lista = eval(plik.read())
                return lista
        else:
            while True:
                plik = self.spr_txt()
                if os.path.exists(plik):
                    with open(plik, "r") as plik:
                        lista = eval(plik.read())
                    return lista
                else:
                    if input("Podany plik nie istnieje czy chcesz wczytać pustą tablice? (T/N): ").lower() == "t":
                        print("odczyt zakończony sukcesem")
                        return []
            self.czyszczenie_ekranu()

    def zawartosc_folderu(self, zmienna = False):
        """

        :param zmienna: True zwraca tablice plików, False zwraca liste print()
        :return: lista plików danego folderu
        """
        dane = self.sciezka_folderu
        print(dane)
        pliki = os.listdir(dane)
        if zmienna == True:
            return pliki
        else:
            print(*pliki, sep=' ')
            return ""

    def info(self, zmienna = False):
        '''
        wyświetla informacje o programie
        :param zmienna: zmienia typ informacji dla True (dokładniejsze)
        :return: zwraca nazwe programu
        '''
        if zmienna == True:
            print("Nazwa: DCS Plugin zapisu")
            print("Autor: Dawid Cisiński")
            print("Wersja:1.0")
            return
        else:
            return "DCS Plugin zapisu v.1.0"
#Autor Dawid Cisiński
