import random
libro = {}
contenidos = ['titulo', 'autor', 'isbn', 'paginas']

def DescribirLibro():
    libro[contenidos[0]] = 'Pajarito azul'
    libro[contenidos[1]] = 'Antoino Perez'
    libro[contenidos[2]] = 'ISBN ' + str(random.randint(100, 999)) + '-' + str(random.randint(0, 9)) + '-' + str(random.randint(100000, 999999)) + '-' + str(random.randint(0, 9))
    libro[contenidos[3]] = str(random.randint(50, 350))

    print(libro)