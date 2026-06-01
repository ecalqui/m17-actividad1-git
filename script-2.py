import time
from dice import roll

def lanzar_dados(amount, sides):
    resultados = []
    for _ in range(amount):
        resultado = roll(f"1d{sides}")
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
<<<<<<< HEAD
    amount = 5
    sides = 20
=======
    amount = 6
    sides = 6
>>>>>>> main
    resultados = lanzar_dados(amount, sides)
    for i, valor in enumerate(resultados, start=1):
        print(f"Lanzamiento {i} número obtenido {valor}")
        time.sleep(5)
