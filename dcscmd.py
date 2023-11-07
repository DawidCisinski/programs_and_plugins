def dcs_cmd(grogcom_info = "info_komend"):
  komendy = {
    "exit": "Wyjście z konsoli.",
    "help": "Podpowiada komendy.",
    "send": "Wymuszenie wysłania danych do programu.",
    "progcom": "[help] / pozwala na komunikacje z programem matką.",
  }

  print("MicroDCS(CMD) [v.1.0]", end="\n\n")

  while True:
    wybor = input(">>>").lower().split(" ")


    if wybor[0] == "send":
      lista = ["send"]
      if len(wybor) > 1:
        if wybor[1] == "str":
          lista.append(wybor[2])
          return lista
        elif wybor[1] == "int":
          lista.append(int(wybor[2]))
          return lista
        elif wybor[1] == "float":
          lista.append(float(wybor[2].replace(",", ".")))
          return lista
        elif wybor[1] == "list" or wybor[1] == "bool":
          lista.append(eval(wybor[2]))
          return lista

    elif wybor[0] == "exit":
      return True

    elif wybor[0] == "progcom":
      if len(wybor) > 1:
        lista = []
        if wybor[1] == "help":
          my_string = grogcom_info.replace("<BREAK!>", "\n")
          print(my_string)
        else:
          lista.append(wybor[1])
          lista.append(wybor[2])
          return lista

    elif wybor[0] == "help":
      print("\nkomendy:")
      for k, v in komendy.items():
        print(k + (12 - len(k)) * " " + v)
      print()
