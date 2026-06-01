import time
from dice import roll

def lanzar_dados(amount, sides):
    resultados = []
    for _ in range(amount):
        resultado = roll(f"1d{sides}")
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    amount = 5
    sides = 6
    resultados = lanzar_dados(amount, sides)
    for i, valor in enumerate(resultados, start=1):
        print(f"Lanzamiento {i} número obtenido {valor}")
        time.sleep(5)
