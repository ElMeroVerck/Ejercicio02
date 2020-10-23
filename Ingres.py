class RegistreUnIngreso:
    def __init__(self):
        self.ReporteDeIngresos = []

    def AgregarUnIngres(self, Abono):
        agregar = str(Abono)
        self.ReporteDeIngresos.append(agregar)

    def verReporte(self):
        return self.ReporteDeIngresos
