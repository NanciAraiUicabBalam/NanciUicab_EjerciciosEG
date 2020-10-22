import re

opcion = 0
while opcion != 11:
 

    print ("\n***************EXPRESIONES REGULARES**************")
    
    print ("\nSeleccionar una opcion")
    print ("\n1.Todas las palabras que tengan una longitud de 7 o más letras\n2.Expresiones que NO finalicen con una vocal.\n3.Las palabras que inicien con “M” donde la segunda letra no sea vocal\n4.Expresiones encerradas entre comillas\n5.Ip’s\n7.Telefonos\n8.Correos electrónicos\n9.Url’s\n10.Código postal\n11.salir ")
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
         filename = "Informacion.txt"
         textFile = open(filename, "r")
         regex = r'\b[a-zA-Z]{7}\b'
         reg = re.compile(regex)
         for line in textFile:
            datos = reg.findall(line)
            print(datos)
         textFile.close()
         
    elif opcion == 2:
         filename = "Informacion.txt"
         textFile = open(filename, "r")
         regex = "[A-Za-z]+"
         reg = re.compile(regex)
         for line in textFile:
          datos= reg.findall(line)
          regex = "[A-Za-z]+[^aeiou]$"
         for elemento in datos:
             if re.search(regex, elemento):
              print(elemento)
         textFile.close()
    elif opcion == 3:
         filename = "Informacion.txt"
         textFile = open(filename, "r")
         regex = "[M][^aeiou][A-Za-z]+"
         reg = re.compile(regex)
         for line in textFile:
             datos = reg.findall(line)
             print(datos)
         textFile.close()
    elif opcion == 4:
         filename = "Informacion.txt"
         textFile = open(filename, "r")
         regex = "(\".*?\"|\'.*?\')"
         reg = re.compile(regex)
         for line in textFile:
             datos = reg.findall(line)
             print(datos)
         textFile.close()
    elif opcion == 5:
         filename = "Informacion.txt"
         textFile = open(filename, "r")
         regex = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
         reg = re.compile(regex)
         for line in textFile:
             datos = reg.findall(line)
             print(datos)
         textFile.close()
    elif opcion == 6:
          filename = "Informacion.txt"
          textFile = open(filename, "r")
          regex = "((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])?)"
          reg = re.compile(regex)
          for line in textFile:
               datos = reg.findall(line)
               print(datos)
          textFile.close()
    elif opcion == 7:
          filename = "Informacion.txt"
          textFile = open(filename, "r")
          regex = "(\+?\d[2]|\(\+?\d[2]\))?(\d{8,12})"
          reg = re.compile(regex)
          for line in textFile:
               datos = reg.findall(line)
               print(datos)
          textFile.close()
    elif opcion == 8:
          filename = "Informacion.txt"
          textFile = open(filename, "r")
          regex = "([a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})+"
          reg = re.compile(regex)
          for line in textFile:
               datos = reg.findall(line)
               print(datos)
          textFile.close()
    elif opcion == 9:
          filename = "Informacion.txt"
          textFile = open(filename, "r")
          regex = "(?:(?:https?|http|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]"
          reg = re.compile(regex)
          for line in textFile:
               datos = reg.findall(line)
               print(datos)
          textFile.close()
    elif opcion == 10:
          filename = "Informacion.txt"
          textFile = open(filename, "r")
          regex = "(\d{5})"
          reg = re.compile(regex)
          for line in textFile:
               datos = reg.findall(line)
               print(datos)
          textFile.close()
          
    elif opcion == 11:
         print("LA OPERACION A CONCLUIDO")
    else:
        print("\nDATO INCORRECTO")
