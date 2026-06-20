MINIMO_INICIAL = 1
MAXIMO_INICIAL = 50
LIMITE_INTENTOS = 5


def mostrar_bienvenida():
    """Muestra las instrucciones iniciales del juego."""
    print()
    print("       JUEGO: ADIVINA EL NÚMERO")
    print()
    print("Piensa un número del 1 al 50.")
    print("La computadora intentará adivinarlo en máximo 5 intentos.")
    print("Responde con: mayor, menor o correcto.")
    print()


def obtener_respuesta():
    """
    Solicita una respuesta válida al usuario.
    Usa un bucle para repetir la pregunta si el usuario escribe una opción incorrecta.
    """
    opciones_validas = ["mayor", "menor", "correcto"]

    while True:
        respuesta = input("Tu respuesta (mayor/menor/correcto): ").lower().strip()

        if respuesta in opciones_validas:
            return respuesta

        print("Respuesta inválida. Escribe solamente: mayor, menor o correcto.")


def jugar():
    """
    Ejecuta la lógica principal del juego.
    Usa búsqueda binaria para calcular cada intento de la computadora.
    """
    minimo = MINIMO_INICIAL
    maximo = MAXIMO_INICIAL
    intentos = 0
    gano_computadora = False

    mostrar_bienvenida()
    input("Cuando ya hayas pensado tu número, presiona ENTER para iniciar...")

    # Bucle principal: se repite mientras no se supere el límite de intentos.
    while intentos < LIMITE_INTENTOS:
        # Si el rango deja de ser válido, significa que hubo respuestas contradictorias.
        if minimo > maximo:
            print("\nLas respuestas no coinciden con un número válido.")
            print("Revisa si respondiste correctamente mayor, menor o correcto.")
            return

        intento = (minimo + maximo) // 2
        intentos += 1

        print(f"\nIntento {intentos}: ¿Tu número es {intento}?")
        respuesta = obtener_respuesta()

        # Condicionales principales según la respuesta del usuario.
        if respuesta == "correcto":
            print("\n¡La computadora ganó!")
            print(f"Adivinó tu número en {intentos} intento(s).")
            gano_computadora = True
            break

        elif respuesta == "mayor":
            # Si el número del usuario es mayor, se actualiza el mínimo.
            minimo = intento + 1

        elif respuesta == "menor":
            # Si el número del usuario es menor, se actualiza el máximo.
            maximo = intento - 1

    if not gano_computadora:
        print("\nLa computadora perdió.")
        print(f"No logró adivinar el número en {LIMITE_INTENTOS} intentos.")


def main():
    """Función principal del programa."""
    jugar()

    # Permite repetir el juego usando un bucle.
    while True:
        repetir = input("\n¿Deseas jugar otra vez? (si/no): ").lower().strip()

        if repetir == "si":
            jugar()
        elif repetir == "no":
            print("\nGracias por jugar. Fin del programa.")
            break
        else:
            print("Opción inválida. Escribe si o no.")


if __name__ == "__main__":
    main()
