#Función que convierte de hexadecimal a decimal
def hex2int(cadena):
    pass

#Función que comprueba si tres distancias pueden formar un triángulo
def forman_triangulo(a, b, c):
    pass

#Función que convierte de decimal a binario
def decimal2binary(integer):
    pass

#Función que calcula la tarifa de taxi para una distancia recorrida dada
def calcular_tarifa(distancia_km):
    pass

#Función que analiza una lista y determina diferentes posibiidades
def analizar_lista(lista):
    pass

def main():
    ######Probando la función hex2int()
    print("Función de hexadecimal a entero:")
    hexa = input("Ingresa un número hexadecimal>> ")
    num = hex2int(hexa)
    print(f"El número {hexa} = {num}\n")

   
    ######Probando la función forman_triangulo()
    print("Función posible triángulo")
    tri = forman_triangulo(4, 6, 3)
    if tri == True:
        print("Se puede formar un triángulo")
    else:
        print("No se puede formar un triángulo")
    print()


    ######Probando la función decimal2binary()
    print("Función Decimal a Binario")
    entero = int(input("Ingrese un número entero: "))
    if entero >= 0:
        binario = decimal2binary(entero)
        print(f"{entero} = {binario}")
    else:
        print("El número ingresado debe ser mayor o igual a cero")

    ######Probando la función calcular_tarifa()
    print("Calculadora de Tarifa de Taxi")
    distancia_km = float(input("Ingrese la distancia recorrida en kilómetros: "))

    if distancia_km >= 0:
        tarifa = calcular_tarifa(distancia_km)
        print(f"La tarifa total del taxi es: ${tarifa}")
    else:
        print("La distancia ingresada no es válida. Debe ser mayor o igual a cero.") 
    
    
    ######Probando la función analizar_lista()
    print("Función para analizar el contenido de una lista")
    mi_lista = [2,34,56,76,-3]
    resultado = analizar_lista(mi_lista)
    print(f"Código: {resultado}")  # Salida esperada: Código: 1

if __name__ == "__main__":
    main()
