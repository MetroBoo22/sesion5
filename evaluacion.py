class Evaluacion:
    """Evaluación de un restaurante: Pendiente -> Verificada -> Publicada (o Rechazada)."""

    def __init__(self, usuario, restaurante, calificacion, comentario):
        self.usuario = usuario
        self.restaurante = restaurante
        self.calificacion = calificacion
        self.comentario = comentario
        self.estado = "Pendiente"

    def verificar(self, consumo_confirmado):
        if not consumo_confirmado:
            self.estado = "Rechazada"
            return False

        if not 1 <= self.calificacion <= 5:
            self.estado = "Rechazada"
            return False

        self.estado = "Verificada"
        return True

    def publicar(self):
        if self.estado == "Verificada":
            self.estado = "Publicada"
            return True
        return False
