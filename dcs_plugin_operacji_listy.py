import os


def str_na_lista(str):
    if "." in str:
        str = str.replace(".", "")
    str += " "
    slowa = []
    miejsce = 0
    for index, i in enumerate(str):
        if i == " ":
            slowa.append(str[miejsce:index])
            miejsce = index + 1
    return slowa


def lista_na_str(lista, separator):
    str = ""
    for index, i in enumerate(lista):
        str = str + separator + i
    return str[1:]


def lista_print(lista):
    for index, obiekt in enumerate(lista):
        print(f"{index + 1}.{obiekt}")


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
