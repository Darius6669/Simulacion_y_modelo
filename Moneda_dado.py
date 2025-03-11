import random

# Constantes
COINS = ["cara", "sello"]  # Opciones posibles para la moneda

def es_numero_par(num):
    """Verifica si un número es par.

    Argumento:
        num (int): Número a verificar.

    Returns:
        bool: True si el número es par, False en caso contrario.
    """
    return num % 2 == 0

def lanzar_dado_y_moneda():
    """Simula el lanzamiento de un dado y una moneda.

        retorna si es True si el dado es par y la moneda es 'cara', False en caso contrario.
    """
    dado = random.randint(1, 6)  # Lanza el dado
    moneda_lanzada = random.choice(COINS)  # Lanza la moneda
    return es_numero_par(dado) and moneda_lanzada == "cara"  # Verifica la condición

def main():
    """Función principal que ejecuta la simulación de lanzamientos."""
    cont_perdidas = 0  # Contador de pérdidas
    cont_ganadas = 0   # Contador de ganancias

    while True:
        try:
            # Solicita al usuario el número de lanzamientos
            num_lanzamientos = int(input("Introduzca el número de veces que se lanzará la moneda y el dado: "))
            if num_lanzamientos <= 0:
                raise ValueError("El número debe ser mayor que cero.")
            break  # Sale del bucle si la entrada es válida
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtelo de nuevo.")  # Mensaje de error

    # Realiza los lanzamientos y cuenta los resultados
    for _ in range(num_lanzamientos):
        if lanzar_dado_y_moneda():
            cont_ganadas += 1  # Incrementa contador de ganancias
        else:
            cont_perdidas += 1  # Incrementa contador de pérdidas

    # Muestra los resultados finales
    print(f"Ganas: {cont_ganadas}, Pierdes: {cont_perdidas}")

# Ejecuta la función principal

main()
