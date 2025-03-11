import random

# Definición de las sentencias posibles según las decisiones de los prisioneros
SENTENCES = {
    ("Confesar", "Confesar"): ("Condena de 5 años", "Condena de 5 años"),
    ("Confesar", "Callar"): ("Libre", "Condena de 20 años"),
    ("Callar", "Confesar"): ("Condena de 20 años", "Libre"),
    ("Callar", "Callar"): ("Condena de 1 año", "Condena de 1 año")
}

DECISIONS = ["Confesar", "Callar"]  # Opciones de decisión para los prisioneros

def tomar_decision():
    """Selecciona aleatoriamente una decisión de los prisioneros.

    Returns:
        str: La decisión tomada ("Confesar" o "Callar").
    """
    return random.choice(DECISIONS)

def main():
    """Función principal que simula el dilema del prisionero."""
    # Obtener las decisiones de los prisioneros
    decision1 = tomar_decision()
    decision2 = tomar_decision()

    print(f"El prisionero 1 ha decidido {decision1}")
    print(f"El prisionero 2 ha decidido {decision2}")

    print("Las respectivas sentencias han sido calculadas...")

    # Determinar el resultado basado en las decisiones
    sentencia1, sentencia2 = SENTENCES[(decision1, decision2)]
    print(f"Prisionero 1: {sentencia1}\nPrisionero 2: {sentencia2}")

# Ejecutar el juego
main()
