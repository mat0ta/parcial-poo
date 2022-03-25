<h1 align="center">PARCIAL-POO</h1>
---

En este [repositorio](https://github.com/mat0ta/parcial-poo) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: mat0ta[https://github.com/mat0ta].

<h2>Libro</h2>

Haz un libro

La función empleada para crear dicho algoritmo es la siguiente:

```py

import random
libro = {}
contenidos = ['titulo', 'autor', 'isbn', 'paginas']

def DescribirLibro():
    libro[contenidos[0]] = 'Pajarito azul'
    libro[contenidos[1]] = 'Antoino Perez'
    libro[contenidos[2]] = 'ISBN ' + str(random.randint(100, 999)) + '-' + str(random.randint(0, 9)) + '-' + str(random.randint(100000, 999999)) + '-' + str(random.randint(0, 9))
    libro[contenidos[3]] = str(random.randint(50, 350))

    print(libro)

```