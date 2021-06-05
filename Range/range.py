def run():
    ''' range(comienzo, final, pasos)'''

    my_range = range(0, 10, 2)
    my_other_range = range(0, 11, 2)
    if my_range == my_other_range:
        calculo = True
    else:
        calculo = False
    print(calculo)

    if my_range is my_other_range:
        calculo = True
    else:
        calculo = False
    print(calculo)

    print(id(my_range))
    print(id(my_other_range))

    for i in range(0, 101, 2):
        print(i + 1)
 





if __name__ == '__main__':
    run()