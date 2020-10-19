
lista = ["Juan", "Alberto", "Jose", "Roman"]
edad = [9,4,1,2]
diccionario_nombres = {"Juan":True, "Alberto":False, "Jose":False, "Roman":True}

for nombre in diccionario_nombres:
    print "Tu nombre es: ",nombre,"Tu edad es: ", diccionario_nombres[nombre]

    if nombre == "Alberto":
        print "Eres gay"
        exit(1)

    elif nombre != "Juan":
        print "No es Juan"

    elif diccionario_nombres[nombre] is True:
        print "Hola"
    else:
        print "Te jodes"


