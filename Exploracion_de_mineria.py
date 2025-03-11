import random

# Probabilidades y ganancias
SUCCESS_PROB = 0.40  # Probabilidad de éxito en una exploración
FAILURE_PROB = 1 - SUCCESS_PROB  # Probabilidad de fallar
COMPANY_SHARE = 0.60  # Porcentaje de ganancia para la empresa
STATE_SHARE = 1 - COMPANY_SHARE  # Porcentaje de ganancia para el estado

# Parámetros de la simulación
BARRELS_PER_SUCCESS = 300000  # Barriles obtenidos por exploración exitosa
EXPLORATION_COST = 1000000  # Costo de cada exploración
BARREL_PRICE = 150  # Precio por barril
TOTAL_EXPLORATIONS = 1000000  # Número total de exploraciones

def exploration_success():
    """Simula el éxito o fracaso de una exploración basado en las probabilidades.

    Returns:
        bool: True si la exploración es exitosa, False en caso contrario.
    """
    return random.random() < SUCCESS_PROB

def simulate_explorations():
    """Simula múltiples exploraciones y calcula los resultados acumulados.

    Returns:
        dict: Un diccionario con los resultados de la simulación.
    """
    total_barrels = 0
    company_balance = -TOTAL_EXPLORATIONS * EXPLORATION_COST  # Inicializa el costo total de exploraciones
    state_balance = 0
    success_count = 0

    for _ in range(TOTAL_EXPLORATIONS):
        if exploration_success():
            success_count += 1
            total_barrels += BARRELS_PER_SUCCESS
            revenue = BARRELS_PER_SUCCESS * BARREL_PRICE
            company_balance += revenue * COMPANY_SHARE
            state_balance += revenue * STATE_SHARE

    # Calcular la tasa de éxito
    success_rate = success_count / TOTAL_EXPLORATIONS
    return {
        "total_barrels": total_barrels,
        "company_balance": company_balance,
        "state_balance": state_balance,
        "success_rate": success_rate,
        "success_count": success_count,
    }

def main():
    """Función principal que ejecuta la simulación y muestra los resultados."""
    results = simulate_explorations()

    print(f"Cantidad de exploraciones realizadas: {TOTAL_EXPLORATIONS}")
    print(f"Cantidad de barriles obtenidos: {results['total_barrels']}")
    print(f"Estado de cuenta de la empresa: {results['company_balance']:.2f}")
    print(f"Total de ganancias del estado: {results['state_balance']:.2f}")
    print(f"Tasa de éxito: {results['success_rate'] * 100:.2f}%")

# Ejecutar la simulación

main()  # Corre la función principal
