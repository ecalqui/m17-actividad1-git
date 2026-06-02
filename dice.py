import random

def roll(expr):
    # expr tiene formato "1d6", "1d20", etc.
    cantidad, caras = expr.lower().split("d")
    cantidad = int(cantidad)
    caras = int(caras)

    total = 0
    for _ in range(cantidad):
        total += random.randint(1, caras)

    return total
