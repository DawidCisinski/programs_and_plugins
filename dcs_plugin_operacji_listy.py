import os

def str_na_liste(str, id = False):
  lista = str.split("<SEP!>")
  if id is not False:
    lista.insert(0,id)
  return lista

#lista.insert(0,id)

def lista_na_str(lista):
  str = "<SEP!>".join(lista)
  return str


def lista_print(lista):
    for index, obiekt in enumerate(lista):
        print(f"{index + 1}.{obiekt}")


def info(zmienna = False):
    '''
    wyświetla informacje o programie
    :param zmienna: zmienia typ informacji dla True (dokładniejsze)
    :return: brak
    '''
    if zmienna == True:
        print("Nazwa: DCS Plugin Operacji Listy")
        print("Autor: Dawid Cisiński")
        print("Wersja:2.0")
        return
    else:
        return "DCS Plugin Operacji Listy v.2.0"


def auto_menu(lista_menu):
    os.system("cls")
    liczby = []
    print("Menu:")
    for index, obiekt in enumerate(lista_menu):
        a = index + 1
        print(f"{a}.{obiekt}")
        liczby.append(str(a))
    print("")
    wybor = input("Wybieram: ").lower()
    if wybor.isalpha():
        if wybor in lista_menu:
           return lista_menu.index(wybor) + 1
        else:
            return "error"
    elif wybor in liczby:
        return wybor
    else:
        return "error"


def menu():
    os.system("cls")
    print("__________")
    print("___Menu___")
    print("1.Operacje")
    print("2.Plik  ")
    print("3.Info   ")
    print("4.Opcje   ")
    print("5.Wyjdź   ")
    print("")
    wybor = input("Wybieram: ").lower()
    print(wybor)
    if wybor == "1" or wybor == "operacje":
        os.system("cls")
        return 1
    elif wybor == "2" or wybor == "plik":
        os.system("cls")
        return 2
    elif wybor == "3" or wybor == "info":
        os.system("cls")
        return 3
    elif wybor == "4" or wybor == "opcje":
        os.system("cls")
        return 4
    elif wybor == "5" or wybor == "wyjdź" or wybor == "wyjdz":
        os.system("cls")
        return 5
    else:
        os.system("cls")
        return 6


def sprawdz_czy_jest_na_liscie(nazwa, lista):
    if nazwa in lista:
        return True
    else:
        return False


def usun_z_listy(nazwa, lista):
    if nazwa in lista and not nazwa.isdigit():
        lista.remove(nazwa)
        return lista
    elif nazwa.isdigit() is True:
        nazwa = int(nazwa)
        if nazwa > 0 and nazwa < len(lista):
            print(len(lista))
            nazwa = nazwa - 1
            lista.pop(nazwa)
            return lista
        else:
            return "error"
    else:
        return "error"


def dodaj_do_listy(nazwa, lista, od_przodu=False):
    if od_przodu == True:
        lista.insert(0, nazwa)
        return lista
    elif nazwa.isalpha():
        lista.append(nazwa)
        return lista
    else:
        lista.append(nazwa)
        return lista


def popraw_na_liscie(nazwa, nowa_nazwa, lista):
    lista[(lista.index(nazwa))] = nowa_nazwa
    return lista


def zamien_na_liscie(nazwa, nazwa2, lista):
    if nazwa in lista:
        nazwa = lista.index(nazwa)
    elif nazwa.isdigit() is True:
        nazwa = int(nazwa)
        if nazwa > 0 and nazwa < len(lista):
            nazwa = nazwa - 1
        else:
            return "error"
    else:
        return "error"
    if nazwa2 in lista:
        nazwa2 = lista.index(nazwa2)
    elif nazwa2.isdigit() is True:
        nazwa2 = int(nazwa2)
        if nazwa2 > 0 and nazwa2 < len(lista):
            nazwa2 = nazwa2 - 1
        else:
            return "error"
    else:
        return "error"
    tmp = lista[nazwa]
    lista[nazwa] = lista[nazwa2]
    lista[nazwa2] = tmp
    return lista

#Dawid Csisiński 

def szybka_lista_na_str(lista):
    return ' '.join(lista)


def wyszukaj_id_na_liscie(lista, id):
  for index, element in enumerate(lista):
    if element[0] == id:
      return index


def ostatnie_id_na_liscie(lista):
  return lista[-1][0]

#len(lista)

#config = {
#    "opcja1":"war1",
#    "opcja2":"war2",
#    "opcja3":"war3",
#}
#print(config["opcja1"])
#a = config.items()
#b = list(a)[0][1]
#print(b)

#for k, v in di: print(v)

#del slownik[“wiek”]
#slownik[“imie”] = “Anna”

def wartosc_slownika(str, slownik):
    if str in slownik:
        return slownik[str]

#Dawid Csisiński 
