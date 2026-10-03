from evaluacion import Evaluacion

LINEA = "=" * 36


def registrar_evaluacion():
    print(f"\n{LINEA}")
    print("            QUE COMO?")
    print("      REGISTRO DE EVALUACIÓN")
    print(LINEA)

    usuario = input("Nombre del comensal: ")
    restaurante = input("Restaurante: ")

    try:
        calificacion = float(input("Calificación (1-5): "))
    except ValueError:
        print("Error: la calificación debe ser un número.")
        return

    comentario = input("Comentario: ")
    consumo = input("¿Existe un consumo, pedido o reserva confirmada? (s/n): ").lower()
    consumo_confirmado = consumo == "s"

    evaluacion = Evaluacion(usuario, restaurante, calificacion, comentario)

    if evaluacion.verificar(consumo_confirmado) and evaluacion.publicar():
        print(f"\n{LINEA}")
        print("       EVALUACIÓN PUBLICADA")
        print(LINEA)
        print("Comensal:", evaluacion.usuario)
        print("Restaurante:", evaluacion.restaurante)
        print("Calificación:", evaluacion.calificacion)
        print("Comentario:", evaluacion.comentario)
        print("Estado:", evaluacion.estado)
        print(LINEA)
    else:
        print(f"\n{LINEA}")
        print("       EVALUACIÓN RECHAZADA")
        print(LINEA)
        if not consumo_confirmado:
            print("Motivo: no existe un consumo confirmado.")
        else:
            print("Motivo: la calificación debe estar entre 1 y 5.")
        print("Estado:", evaluacion.estado)
        print(LINEA)


if __name__ == "__main__":
    registrar_evaluacion()
