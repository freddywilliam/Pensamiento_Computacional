def run():
    
    print(''' 
    Clonar lista
    
    ''')
    a = [1, 2, 3, 4]
    b = list(a)
    c = a[::]
    print("Lista A: " + str(a) + " id: " + str(id(a)))
    print("Lista B: " + str(b) +" id: " + str(id(b)))
    print("Lista C: " + str(c) + " id: " + str(id(c)))

    print(''' 
    
    LIST COMPREHENSION
    
     ''')
    my_list = list(range(100))
    print(my_list)

    print(''' 
    
    Multiplico cada valor de la lista x 2 
    
    ''')
    double = [i * 2 for i in my_list]
    print(double)

    print('''
    
    Unicamente los pares
    
    ''')
    pares = [i for i in my_list if i % 2 == 0]
    print(pares)

if __name__ =='__main__':
    run()

