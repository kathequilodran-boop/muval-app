# Proyecto simple: MuVal – Mujer Valiente

def bienvenida(nombre):
    return f"Bienvenida {nombre} a MuVal - Mujer Valiente 💜"

def menu():
    print("=== MuVal App ===")
    nombre = input("Ingresa tu nombre: ")
    print(bienvenida(nombre))

menu()
