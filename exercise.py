import random
import string

#Hola Mundo: escribir un programa que imprima “Hola Mundo” en la terminal/consola.
hello = "Hello world"
print(hello)
#Calculadora: escribir un programa que tome dos números como entrada y realice operaciones básicas como suma, resta y multiplicación
numberOne = 4
numberTwo = 8
sum = numberOne + numberTwo
rest = numberOne - numberTwo
mult = numberOne * numberTwo
divi = numberOne / numberTwo
print (sum)
print (rest)
print(mult)
print(divi)
# Contador de palabras: escribe un programa que cuente el número de palabras en una cadena de texto dada.
words = ['hola','arbol','nope']
def contWord(word): #creamos una función contador con el parametro word ._.
  "cuenta el número de palabras"
  return len(word) #len para que de inmediato vea el tamaño elementos de un array

numberWord = contWord(words)#asignamos una variable que contendrá la función, pasando como argumento el array
print(numberWord) #cuando imprima ejecutará la función, lo que nos dará el número de elemento de la variable que pasamos com argumento

#Adivina el número: escribe un programa que genere un número aleatorio y que permita al usuario adivinar cuál es. Proporcionar pistas como “Demasiado alto” y “Demasiado bajo” hasta que el usuario adivine el número.

def number_Random():
  ran_Number = random.randint(30,35)
  riddle = None
  attempts = 0

  print("hola bienvenido al juego")

  while riddle != ran_Number:
    try:
      riddle = int(input("insertar número :"+ " "))
      attempts += 1
      if riddle < ran_Number:
        print("El número está por debajo del indicado")
      elif riddle > ran_Number:
        print("El número está por encima del correcto")
    except ValueError:
        print("introduce un valor entre los indicados")


  print(f"felicidades has encontrado el número {ran_Number} en {attempts} intentos ")

if __name__ == "__main__":
    number_Random()

#Listado de tareas: escribe un programa que permita al usuario agregar, eliminar, y mostrar una lista de tareas pendientes.

list_works = ["barrer", "lavar platos", "sacar la basura"]

def add_work(works=None):
    if works is None:
        works = list_works

    print("La lista de tareas es:")
    for work in works:
        print(f"- {work}")

    add_new = input("Agrega una nueva tarea: ")
    works.append(add_new)

    print("La lista de tareas actualizada es:")
    for work in works:
        print(f"- {work}")
    
    delete_work = input("¿Deseas eliminar una tarea que ya completaste? (si/no): ")
    res_decline = "no"
    res_confirm = "si"
    
    if delete_work == res_confirm:
        response = input("Introduce la tarea que deseas eliminar: ")
        if response in works:
            works.remove(response)
            print("Tarea eliminada.")
            print("La lista actualizada es:")
            for work in works:
                print(f"- {work}")
        else:
            print("La tarea no se encontró en la lista.")
    
    elif delete_work == res_decline:
        print("La lista actualizada es:")
        for work in works:
            print(f"- {work}")

if __name__ == "__main__":
    add_work()



# Generador de contraseñas: escribe un programa que genere una contraseña aleatoria de una longitud especificada por el usuario. Esta debe contener letras, números, y caracteres especiales


def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def main():
    longitud = int(input("Introduce la longitud deseada para la contraseña: "))
    contraseña = generar_contraseña(longitud)
    print("Tu contraseña generada es:", contraseña)

if __name__ == "__main__":
    main()


