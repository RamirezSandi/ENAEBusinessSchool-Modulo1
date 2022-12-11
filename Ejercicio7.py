# EJERCICIO 7 >> Encontrar una lista de 73 numeros no primos seguidos

x=0
counter = 0
lista_no_primos = []

# el siguiente loop se va a repetir hasta encontrar una secuencia de 73 numeros no primos
while (counter < 73):
  #primero reviso si es o no primo
    for i in range(2,x):
      if x % i == 0:
        #en caso que no sea primo, sumo 1 a mi counter y agrego el nuevo no'primo a la lista
        counter = counter + 1
        lista_no_primos.append(x)
        break

    if i == x-1:
      #en caso que encuentre un primo antes de llegar a una seuencia de 73, reinicio la lista y sigo con el siguiente numero
      counter = 0
      lista_no_primos = []
    x = x + 1

print("El intervalo de numeros no primos es: ")
print(lista_no_primos)
print("El tamaño de la lista es: " + str(len(lista_no_primos)))
