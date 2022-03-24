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