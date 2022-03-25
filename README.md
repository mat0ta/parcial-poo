<h1 align="center">PARCIAL-POO</h1>
---
En este [repositorio](https://github.com/mat0ta/parcial-poo) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: mat0ta[https://github.com/mat0ta].
<h2>Libro</h2>
Haz un creador de libros
La funci�n empleada para crear dicho algoritmo es la siguiente:
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
```<h2>Animales</h2>
Haz un organizador de animales
La funci�n empleada para crear dicho algoritmo es la siguiente:
```py
objetos = ['Animal', 'Mamífero', 'Ovíparo', 'Pollo', 'Gato', 'Ornitorrinco']
diccionario = {}

def Declaracion():
    global objetos
    for i in range(len(objetos)):
        if objetos[i] == 'Animal':
            diccionario[objetos[i]] = {}
        elif objetos[i] == 'Mamífero' or objetos[i] == 'Ovíparo':
            diccionario['Animal'][objetos[i]] = {}
        elif objetos[i] == 'Pollo' or objetos[i] == 'Ornitorrinco':
            diccionario['Animal']['Ovíparo'][objetos[i]] = {}
        elif objetos[i] == 'Gato':
            diccionario['Animal']['Mamífero'][objetos[i]] = {}
        print(diccionario)
```<h2>Bando</h2>
Han un banco con sistemas
La funci�n empleada para crear dicho algoritmo es la siguiente:
```py
import random, datetime, names
from secrets import randbits
from shutil import register_unpack_format
from faker import Faker
fake = Faker()

cuentas = {}
nextId = 0
saldo_negativo_maximo = -10000
fecha_plazo_fijo = fake.date_between(start_date=datetime.date(year=2022, month=4, day=1), end_date='+2y')

def crearCuenta(numero_de_cuentas = 1, tipo = 'Normal'):
    global cuentas, nextId
    for i in range(numero_de_cuentas):
        dinero_inicial = random.randint(10000, 1000000)
        numero_de_cuenta = random.randint(100000000000, 999999999999)
        inicio_creacion = datetime.date(year=2008, month=1, day=1)
        apertura = fake.date_between(start_date=inicio_creacion, end_date='+12y')
        inicio_vencimiento = datetime.date(year=2022, month=1, day=1)
        venicmiento = fake.date_between(start_date=inicio_vencimiento, end_date='+12y')
        for i in range(nextId - 1):
            while cuentas[i]['IBAN'] == numero_de_cuenta:
                numero_de_cuenta = random.randint(100000000000, 999999999999)
        cuentas[nextId] = {
            'Nombre': names.get_full_name(),
            'IBAN': numero_de_cuenta,
            'Saldo': dinero_inicial,
            'Tipo': tipo,
            'Fecha de Apertura': apertura.strftime("%m/%d/%Y"),
            'Fecha de Vencimiento': venicmiento.strftime("%m/%d/%Y")
        }
        nextId = nextId + 1
        print(nextId)
    print(cuentas)

def retirar(iban, cantidad):
    global cuentas, nextId
    for i in range(nextId):
        if cuentas[i]['IBAN'] == iban:
            if cuentas[i]['Saldo'] >= cantidad:
                if cuentas[i]['Tipo'] == 'Plazo Fijo':
                    if datetime.date.today() <= fecha_plazo_fijo:
                        cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad
                    else:
                        cantidad_ = cantidad + (cantidad * 0.05)
                        cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad_
                        return print('Se han retirado ' + str(cantidad) + '.-€ de la cuenta ' + str(iban) + ' exitosamente con una penalización del 5%.\nSaldo actual: ' + str(cuentas[i]['Saldo']) + '.-€')
                cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad
                return print('Se han retirado ' + str(cantidad) + '.-€ de la cuenta ' + str(iban) + ' exitosamente.\nSaldo actual: ' + str(cuentas[i]['Saldo']) + '.-€')
            elif cuentas[i]['Tipo'] == 'VIP' and cuentas[i]['Saldo'] - cantidad >= saldo_negativo_maximo:
                cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad
                return print('Se han retirado ' + str(cantidad) + '.-€ de la cuenta VIP ' + str(iban) + ' exitosamente.\nSaldo actual: ' + str(cuentas[i]['Saldo']) + '.-€')
            else:
                return print('La cuenta no tiene suficiente saldo para retirar esa cantidad de dinero.\nSaldo actual: ' + str(cuentas[i]['Saldo']) + '.-€')
    print('La cuenta' + str(iban) + ' no existe.')

def ingresar(iban, cantidad):
    global cuentas, nextId
    for i in range(nextId):
        if cuentas[i]['IBAN'] == iban:
            cuentas[i]['Saldo'] = cuentas[i]['Saldo'] + cantidad
            return print('Se han ingresado ' + str(cantidad) + '.-€ en la cuenta ' + str(iban) + ' exitosamente.\nSaldo actual: ' + str(cuentas[i]['Saldo']) + '.-€')
    print('La cuenta' + str(iban) + ' no existe.')

def transferir(emisor, receptor, cantidad):
    global cuentas, nextId
    for i in range(nextId):
        if cuentas[i]['IBAN'] == emisor:
            if cuentas[i]['Saldo'] >= cantidad:
                for j in range(nextId):
                    if cuentas[j]['IBAN'] == receptor:
                        if cuentas[i]['Tipo'] == 'Plazo Fijo':
                            cantidad_ = cantidad + (cantidad * 0.05)
                            cuentas[j]['Saldo'] = cuentas[j]['Saldo'] + cantidad
                            cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad_
                            return print('Se han trasferido de forma exitosa ' + str(cantidad) + '.-€ de la cuenta ' + str(emisor) + ' con un 5% de penalización a la cuenta ' + str(receptor) + '\nSaldo cuenta "' + str(emisor) + '": ' + str(cuentas[i]['Saldo']) + '.-€' + '\nSaldo cuenta "' + str(receptor) + '": ' + str(cuentas[j]['Saldo']) + '.-€' )
                        cuentas[j]['Saldo'] = cuentas[j]['Saldo'] + cantidad
                        cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad
                        return print('Se han trasferido de forma exitosa ' + str(cantidad) + '.-€ de la cuenta ' + str(emisor) + ' a la cuenta ' + str(receptor) + '\nSaldo cuenta "' + str(emisor) + '": ' + str(cuentas[i]['Saldo']) + '.-€' + '\nSaldo cuenta "' + str(receptor) + '": ' + str(cuentas[j]['Saldo']) + '.-€' )
                return print('La cuenta del receptor no existe.')
            elif cuentas[i]['Tipo'] == 'VIP' and cuentas[i]['Saldo'] - cantidad >= saldo_negativo_maximo:
                for j in range(nextId):
                    if cuentas[j]['IBAN'] == receptor:
                        cuentas[j]['Saldo'] = cuentas[j]['Saldo'] + cantidad
                        cuentas[i]['Saldo'] = cuentas[i]['Saldo'] - cantidad
                        return print('Se han trasferido de forma exitosa ' + str(cantidad) + '.-€ de la cuenta ' + str(emisor) + ' a la cuenta ' + str(receptor) + '\nSaldo cuenta "' + str(emisor) + '": ' + str(cuentas[i]['Saldo']) + '.-€' + '\nSaldo cuenta "' + str(receptor) + '": ' + str(cuentas[j]['Saldo']) + '.-€' )
                return print('La cuenta del receptor no existe.')
            else:
                return print('No tiene suficiente saldo para realizar esta transacción.')
    return print('La cuenta del emisor no existe.')

# crearCuenta()
# retirar(cuentas[nextId - 3]['IBAN'], cuentas[nextId - 3]['Saldo'] + 3000)
# ingresar(cuentas[nextId - 4]['IBAN'], 1000)
# transferir(cuentas[nextId - 4]['IBAN'], cuentas[nextId - 3]['IBAN'], 1000)

def aplicacion():
    iban = []
    numero_de_cuentas = int(input('Bienvenido al Banco VVBA. Por favor, introduzca el número de cuentas que quiere crear: '))
    cuentas_vip = int(input('Ahora introduzca el número de cuentas que quiere que sean VIP: '))
    cuentas_plazo_fijo = int(input('Ahora introduzca el número de cuentas que quiere que sean a Plazo Fijo: '))
    while cuentas_vip > numero_de_cuentas: 
        cuentas_vip = int(input('Introduzca el número de cuentas que quiere que sean VIP que sea menor al número de cuentas creadas: '))
    while cuentas_plazo_fijo > numero_de_cuentas: 
        cuentas_plazo_fijo = int(input('Introduzca el número de cuentas que quiere que sean a Plazo Fijo que sea menor al número de cuentas creadas: '))
    for i in range(cuentas_vip):
        crearCuenta(1, 'VIP')
    for i in range(cuentas_vip):
        crearCuenta(1, 'Plazo Fijo')
    cuentas_especiales = cuentas_vip + cuentas_plazo_fijo
    for i in range(numero_de_cuentas - cuentas_especiales):
        crearCuenta(1, 'Normal')
    for i in range(nextId - 1):
        iban.append(cuentas[i]['IBAN'])
    retirar(cuentas[nextId - random.randint(1, numero_de_cuentas)]['IBAN'], 78)
    ingresar(cuentas[nextId - random.randint(1, numero_de_cuentas)]['IBAN'], 575)
    transferir(cuentas[nextId - random.randint(1, numero_de_cuentas)]['IBAN'], cuentas[nextId - random.randint(1, numero_de_cuentas)]['IBAN'], 2000)
    
```