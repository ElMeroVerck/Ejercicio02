class RegistreUnEgreso:
    def __init__(self):
        self.ReporteDeEgresos = []

    def AgregarUnEgreso(self, Retiro):
        agregar = str(Retiro)
        self.ReporteDeEgresos.append(agregar)

    def verReporte(self):
        return self.ReporteDeEgresos
