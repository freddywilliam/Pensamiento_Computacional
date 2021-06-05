def run():
    
    my_dict = {
        'David' : 10,
        'Pedro' : 11,
        'Sara' : 18,
        'Fulana' : 20,
    }
    print(''' 
    -----------------------------------------------------------------------------------

    AQUI USO "my_dict.get('nombre de llave', 'o no existe') " PARA BUSCAR EL VALOR DE LAS LLAVES

    ''')

    print(my_dict.get('David', 'No hay'))
    print(my_dict.get('Pepsi', 'No hay Pepsi'))

    print('''
    -------------------------------------------------------------------------
    
    AQUI USO "my_dict['Sara'] = 20" PARA EDITAR VALOR DE LA LLAVE 

    ''')

    my_dict['Sara'] = 21
    print(my_dict['Sara'])

    print('''
    -------------------------------------------------------------------------
    
    AQUI USO "my_dict['Anchoa'] = 7" PARA AGREGAR ITEMS 
    
    ''')
    my_dict['Anchoa'] = 40
    print(my_dict)

    print('''
    --------------------------------------------------------------------------------
    
    AQUI USO "del my_dict['Pedro']" PARA ELIMINAR
    
    ''')

    del my_dict['Pedro']
    print(my_dict)

    print('''
    ===================================================================

     ITERACIONES!!!
     
     ''')

    print('''
    ---------------------------------------------------------------------
    
     AQUI USO "for llaves in my_dict.keys(): PARA MOSTRAR LAS LLAVES
     
     ''')

    for llaves in my_dict.keys():
        print(llaves)

    print(''' 
    -------------------------------------------------------------------------
    
    AQUI USO " for valor in my_dict.values(): " PARA MOSTRAR VALORES DE LAS LLAVES
    
    ''')

    for valor in my_dict.values():
        print(valor)
    
    print(''' 
    -------------------------------------------------------------------------------
    
    AQUI USO " for llaves, valor in my_dict.items(): " PARA MOSTRAR LLAVES Y VALORES DE LAS LLAVES
    
    ''')
    
    for llaves, valor  in my_dict.items():
        print(llaves, valor)

if __name__ =='__main__':
    run()