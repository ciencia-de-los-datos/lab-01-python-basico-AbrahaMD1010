"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

def pregunta_01():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    sum = 0
    for row in relacion:
        sum += int(row[1])

    return sum

print("\nPregunta 1")
print(pregunta_01())



"""
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

def pregunta_02():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if fila[0] not in dic.keys():
            dic[fila[0]] = 1
        else:
            dic[fila[0]] +=1

        tuplas = list(dic.items())
        tuplas.sort(key=lambda x: x[0])

    return tuplas

print("\nPregunta 2")
print(pregunta_02())


"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
def pregunta_03():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if fila[0] not in dic.keys():
            dic[fila[0]] = int(fila[1])
        else:
            dic[fila[0]] += int(fila[1])

        tuplas = list(dic.items())
        tuplas.sort(key=lambda x: x[0])

    return tuplas

print("\nPregunta 3")
print(pregunta_03())

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
def pregunta_04():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if fila[2][5:7] not in dic.keys():
            dic[fila[2][5:7]] = 1
        else: 
            dic[fila[2][5:7]] +=1

    tuplas = list(dic.items())
    tuplas.sort(key=lambda x:x[0])

    return tuplas

print("\nPregunta 4")
print(pregunta_04())



"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
def pregunta_05():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if fila[0] not in dic.keys():
            dic[fila[0]] = []
            dic[fila[0]].append(int(fila[1]))
        else:
            dic[fila[0]].append(int(fila[1]))

    tuplas = [(key, max(values), min(values)) for key, values in dic.items()]
    tuplas.sort(key=lambda x: x[0])
    return tuplas

print("\nPregunta 5")
print(pregunta_05())

"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
def pregunta_06():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        fila[-1] = fila[-1].rstrip("\n")  # Eliminar el salto de línea al final
        separados = fila[-1].split(",")

        for elemento in separados:
            if elemento[0:3] not in dic.keys():
                dic[elemento[0:3]] = []
                dic[elemento[0:3]].append(int(elemento[4:]))
            else: 
                dic[elemento[0:3]].append(int(elemento[4:]))

        tuplas = [(key, min(values), max(values)) for key, values in dic.items()]
        tuplas.sort(key=lambda x: x[0])
    return tuplas

print("\nPregunta 6")
print(pregunta_06())

"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
def pregunta_07():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if fila[1] not in dic.keys():
            dic[fila[1]] = []
            dic[fila[1]].append(fila[0])
        else:
            dic[fila[1]].append(fila[0])

    tuplas = list(dic.items())
    tuplas.sort(key=lambda x:x[0])

    return tuplas

print("\nPregunta 7")
print(pregunta_07())

"""
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

def pregunta_08():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        if int(fila[1]) not in dic.keys():
            dic[int(fila[1])] = []
            dic[int(fila[1])].append(fila[0])
        elif fila[0] not in dic[int(fila[1])]:
            dic[int(fila[1])].append(fila[0])

    tuplas = [(key, sorted(values)) for key, values in dic.items()]
    tuplas.sort(key=lambda x: x[0])
    

    return tuplas

print("\nPregunta 8")
print(pregunta_08())

"""
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

def pregunta_09():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        fila[-1] = fila[-1].rstrip("\n")
        separados = fila[-1].split(",")

        for elemento in separados:
            if elemento[0:3] not in dic.keys():
                dic[elemento[0:3]] = 1
            else:
                dic[elemento[0:3]] +=1
    dic = dict(sorted(dic.items(), key=lambda x: x[0]))

    return dic

print("\nPregunta 9")
print(pregunta_09())

"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

def pregunta_10():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    tuplas = []
    for fila in relacion:
        tuplas.append((fila[0], len(fila[-2].split(",")), len(fila[-1].split(","))))

    return tuplas

print("\nPregunta 10")
print(pregunta_10())

"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

def pregunta_11():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        separados = fila[-2].split(",")

        for letra in separados:
            if letra not in dic.keys():
                dic[letra] = int(fila[1])
            else:
                dic[letra] += int(fila[1])

    dic = dict(sorted(dic.items(), key=lambda x: x[0]))

    return dic

print("\nPregunta 11")
print(pregunta_11())

"""
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

def pregunta_12():
    with open("data.csv", "r") as file:
        relacion = file.readlines()
        relacion = [line.split("\t") for line in relacion]

    dic = {}
    for fila in relacion:
        fila[-1] = fila[-1].rstrip("\n")
        separados = fila[-1].split(",")

        for elemento in separados:
            if fila[0] not in dic.keys():
                dic[fila[0] ] = int(elemento[4:])
            else:
                dic[fila[0] ] += int(elemento[4:])

    dic = dict(sorted(dic.items(), key=lambda x: x[0]))
    return dic

print("\nPregunta 12")
print(pregunta_12())