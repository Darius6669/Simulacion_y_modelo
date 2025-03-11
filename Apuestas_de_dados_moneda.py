import random

# Constantes
INICIAL = 1000
META = 2000
NUM_JUEGOS = 100

def es_numero_par(num):
    """Verifica si un número es par."""
    return num % 2 == 0

def jugar(monedas, apuesta):
    """Simula una ronda de juego y actualiza las monedas.

    Args:
        monedas (int): Cantidad de monedas del jugador.
        apuesta (int): Cantidad apostada en esta ronda.

    Returns:
        int: Nuevas monedas después de la ronda.
    """
    dado = random.randint(1, 6)
    moneda_lanzada = random.choice(["cara", "sello"])
    es_par = es_numero_par(dado)

    if es_par and moneda_lanzada == "cara":
        return monedas + apuesta
    return monedas - apuesta

def simular_juego(apuesta_inicial):
    """Simula un juego hasta alcanzar la meta o perder todas las monedas.

    Args:
        apuesta_inicial (int): Monto inicial de la apuesta.

    Returns:
        bool: True si se alcanza la meta, False si se pierden todas las monedas.
    """
    monedas = INICIAL
    apuesta = apuesta_inicial

    while monedas < META and monedas > 0:
        inicial = monedas
        monedas = jugar(monedas, apuesta)

        # Ajustar la apuesta
        if monedas < inicial:
            apuesta = min(apuesta * 2, monedas)  # Duplicar la apuesta, pero no exceder monedas
        else:
            apuesta = apuesta_inicial  # Reiniciar a la apuesta inicial

    return monedas >= META  # Retorna True si se alcanzó la meta

def main():
    """Función principal para ejecutar la simulación de juegos."""
    while True:
        try:
            apuesta_inicial = float(input("Introduzca su apuesta inicial: "))
            if apuesta_inicial <= 0:
                raise ValueError("La apuesta debe ser un número positivo.")
            break
        except ValueError as e:
            print(e)

    cont_ganadas = 0
    cont_perdidas = 0

    for _ in range(NUM_JUEGOS):
        if simular_juego(apuesta_inicial):
            cont_ganadas += 1
        else:
            cont_perdidas += 1

    print("Ganadas:", cont_ganadas, "Perdidas:", cont_perdidas)

main()  # Ejecuta la función principal
