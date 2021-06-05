def lista_palabras(lista):
    primera_letra = []

    for palabra in lista:
        assert type(palabra) == str, palabra + ' No es una palabra. '
        assert len(palabra) > 0,  'No se permite espacios en blanco. '

        primera_letra.append(palabras[0])