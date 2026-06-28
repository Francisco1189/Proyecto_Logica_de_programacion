MINIMO_INICIAL = 1
MAXIMO_INICIAL = 50
LIMITE_INTENTOS = 5

# Estructura de datos principal:
# lista que guarda todas las partidas jugadas.
historial_partidas = []


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print()
    print("       JUEGO: ADIVINA EL NÚMERO")
    print()
    print("1. Jugar")
    print("2. Ver historial")
    print("3. Ver estadísticas")
    print("4. Salir")
    print()


def mostrar_bienvenida():
    """Muestra las instrucciones iniciales del juego."""
    print()
    print("Piensa un número del 1 al 50.")
    print("La computadora intentará adivinarlo en máximo 5 intentos.")
    print("Responde con: mayor, menor o correcto.")
    print()


def obtener_opcion_menu():
    """
    Solicita una opción válida del menú.
    Utiliza manejo de excepciones para validar la entrada.
    """
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion in [1, 2, 3, 4]:
                return opcion

            print("Opción inválida. Debe elegir entre 1 y 4.")

        except ValueError:
            print("Error: Debe ingresar únicamente un número.")


def obtener_respuesta(opciones_validas):
    """
    Solicita una respuesta válida al usuario.
    Usa manejo de excepciones y valida la entrada del usuario.
    """
    while True:
        try:
            respuesta = input(
                "Tu respuesta (mayor/menor/correcto): "
            ).lower().strip()

            if respuesta in opciones_validas:
                return respuesta

            raise ValueError

        except ValueError:
            print("Respuesta inválida. Escribe solamente mayor, menor o correcto.")


def registrar_partida(numero_partida, resultado, intentos, detalle_intentos):
    """
    Guarda los datos de cada partida en un diccionario.
    Luego agrega ese diccionario a la lista historial_partidas.
    """
    partida = {
        "numero_partida": numero_partida,
        "resultado": resultado,
        "intentos": intentos,
        "detalle_intentos": detalle_intentos
    }

    historial_partidas.append(partida)


def mostrar_historial():
    """Muestra el historial de todas las partidas jugadas."""
    if len(historial_partidas) == 0:
        print("\nNo hay partidas registradas.")
        return

    print()
    print("       HISTORIAL DE PARTIDAS")

    for partida in historial_partidas:
        print()
        print(f"Partida #{partida['numero_partida']}")
        print(f"Resultado: {partida['resultado']}")
        print(f"Intentos utilizados: {partida['intentos']}")
        print("Detalle de intentos:")

        for intento in partida["detalle_intentos"]:
            print(
                f"  Intento {intento['numero_intento']}: "
                f"la computadora propuso {intento['numero_propuesto']} "
                f"y el usuario respondió '{intento['respuesta']}'"
            )


def mostrar_estadisticas():
    """Calcula y muestra estadísticas generales usando el historial."""
    if len(historial_partidas) == 0:
        print("\nNo hay estadísticas disponibles porque aún no hay partidas.")
        return

    total_partidas = len(historial_partidas)
    partidas_ganadas = 0
    partidas_perdidas = 0
    partidas_con_error = 0
    total_intentos = 0

    for partida in historial_partidas:
        total_intentos += partida["intentos"]

        if partida["resultado"] == "Ganó la computadora":
            partidas_ganadas += 1
        elif partida["resultado"] == "Perdió la computadora":
            partidas_perdidas += 1
        else:
            partidas_con_error += 1

    promedio_intentos = total_intentos / total_partidas

    estadisticas = {
        "total_partidas": total_partidas,
        "partidas_ganadas": partidas_ganadas,
        "partidas_perdidas": partidas_perdidas,
        "partidas_con_error": partidas_con_error,
        "promedio_intentos": promedio_intentos
    }

    print()
    print("       ESTADÍSTICAS DEL JUEGO")
    print()
    print(f"Total de partidas: {estadisticas['total_partidas']}")
    print(f"Partidas ganadas por la computadora: {estadisticas['partidas_ganadas']}")
    print(f"Partidas perdidas por la computadora: {estadisticas['partidas_perdidas']}")
    print(f"Partidas con respuestas contradictorias: {estadisticas['partidas_con_error']}")
    print(f"Promedio de intentos utilizados: {estadisticas['promedio_intentos']:.2f}")


def jugar(numero_partida):
    """
    Ejecuta la lógica principal del juego.
    Usa búsqueda binaria y estructuras de datos para registrar los intentos.
    """
    minimo = MINIMO_INICIAL
    maximo = MAXIMO_INICIAL
    intentos = 0
    gano_computadora = False

    detalle_intentos = []
    opciones_validas = ["mayor", "menor", "correcto"]

    mostrar_bienvenida()
    input("Cuando ya hayas pensado tu número, presiona ENTER para iniciar...")

    while intentos < LIMITE_INTENTOS:

        if minimo > maximo:
            print("\nLas respuestas no coinciden con un número válido.")
            print("Revisa si respondiste correctamente mayor, menor o correcto.")

            registrar_partida(
                numero_partida,
                "Partida finalizada por respuestas contradictorias",
                intentos,
                detalle_intentos
            )
            return

        intento = (minimo + maximo) // 2
        intentos += 1

        print(f"\nIntento {intentos}: ¿Tu número es {intento}?")
        respuesta = obtener_respuesta(opciones_validas)

        detalle_intentos.append({
            "numero_intento": intentos,
            "numero_propuesto": intento,
            "respuesta": respuesta
        })

        if respuesta == "correcto":
            print("\n¡La computadora ganó!")
            print(f"Adivinó tu número en {intentos} intento(s).")
            gano_computadora = True

            registrar_partida(
                numero_partida,
                "Ganó la computadora",
                intentos,
                detalle_intentos
            )
            break

        elif respuesta == "mayor":
            minimo = intento + 1

        elif respuesta == "menor":
            maximo = intento - 1

    if not gano_computadora:
        print("\nLa computadora no logró adivinar el número.")
        print(f"Se alcanzó el límite de {LIMITE_INTENTOS} intentos.")

        registrar_partida(
            numero_partida,
            "Perdió la computadora",
            intentos,
            detalle_intentos
        )


def main():
    """Función principal del programa."""
    numero_partida = 1

    while True:
        try:
            mostrar_menu()
            opcion = obtener_opcion_menu()

            if opcion == 1:
                jugar(numero_partida)
                numero_partida += 1

            elif opcion == 2:
                mostrar_historial()

            elif opcion == 3:
                mostrar_estadisticas()

            elif opcion == 4:
                print("\nGracias por jugar. Fin del programa.")
                break

        except KeyboardInterrupt:
            print("\n\nPrograma finalizado por el usuario.")
            break


if __name__ == "__main__":
    main()
