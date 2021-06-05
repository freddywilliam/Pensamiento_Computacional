
def run():
    print(''' 
    ---------------------------------------------------
    
    AQUI CREO MI DICCIONARIO 
    
    ''')

    dict = {
        'david' : 18,
        'pedro' : 20,
        'sara' : 10,
        'melissa' : 17,
    }
    print(dict)

    print('''
    ---------------------------------------------------------


     AQUI CREO UNA VARIABLE Y EN ELLA ASIGNO DEFINO:
    
        name:age  = Seria la estructura, en ella puedo agregar cosas como el ".capitalize".
        
        for name, age in dict.items():  = Defino las partes que quiero que iteren dentro de dict.
        
        if age > 18 = Quiero que solo iteractue los que sean mayores a 18.


        ''')
    d = {
     
        name.capitalize(): age
        for name, age in dict.items()
        if age >= 18
    }
    print('''
    -------------------------------------------------------------
    
     AQUI SOLAMENTE IMPRIMO LA VARIABLE "d" EN ELLA ESTA TODO EL PROCESO
     
     ''')
    print(d)


if __name__ == '__main__':
    run()