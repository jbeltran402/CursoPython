# cumple la funcion de un swtch, pero con la posibilidad de identificar diccionarios

usuario = {"nombre":"Apellido",
           "edad":45,
           "ocupacion" : "instructor"}
pelicula = {"titulo":"Matrix",
            "ficha_tecnica":{"protagonista":"keanu",
                           "director":"lana y lily"}}
elementos = [usuario,pelicula,"libro"]

for e in elementos:
    match e:
        case{"nombre":nombre,
             "edad": edad,
             "ocupacion": ocupacion}:
            print("Es un usuario")
        case {"titulo": titulo,
              "ficha_tecnica":{"protagonista":protagonista,
                              "director":director}}:
            print("es una pelicula")
        case _:
            print("No sé que es esto")