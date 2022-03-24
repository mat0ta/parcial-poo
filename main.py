import sys
sys.path.insert(1, './modules')
from modules import Libro, Animales, Banco

array_ejercicios = {
  1: 'Libro.DescribirLibro()',
  2: 'Animales.Declaracion()',
  3: 'Banco.aplicacion()',
}

if __name__ == "__main__":
  start = input('Bienvenido a la plataforma de ejercicios del Parcial de POO. Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')
  while int(start) >= 1 and int(start) <= 3:
    eval(str(array_ejercicios[int(start)]))
    start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')