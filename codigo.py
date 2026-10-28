from abc import ABC, abstractmethod
class Estudiante(ABC):
    def __init__(self, nombre, monto_pagado=0):
        self.__nombre=nombre
        self.__monto_pagado=monto_pagado
    @property
    def nombre(self):
        return self.__nombre
    @property
    def monto_pagado(self):
        return self.__monto_pagado
    def registrar_pago(self, monto):
        self.__monto_pagado +=monto
    @abstractmethod
    def calcular_total(self):
        pass
    def mostrar_datos(self):
        total = self.calcular_total()
        print(f"Estudiante: {self.nombre}")
        print(f"Monto que corresponde pagar: S/ {total:.2f}")
        print(f"Monto pagado: S/ {self.monto_pagado:.2f}")
        print(f"Saldo pendiente: S/{max(0, total -self.monto_pagado):.2f}")
        print("-" * 40)
class MatriculaExtemporanea:
    def cargo_matricula(self):
        return 15.00
class IndiceDesaprobatorio:
    def cargo_indice(self):
        return 15.00
class BecaViolencia:
    def aplicar_beca(self, monto):
        return monto / 2
class EstudianteRegular(Estudiante):
    def calcular_total(self):
        return 60.00
class EstudianteExtemporaneo(Estudiante, MatriculaExtemporanea):
    def calcular_total(self):
        return 60.00 +self.cargo_matricula()
class EstudianteDesaprobado(Estudiante, IndiceDesaprobatorio):
    def calcular_total(self):
        return 60.00 +self.cargo_indice()
class EstudianteBecario(Estudiante, BecaViolencia):
    def calcular_total(self):
        return self.aplicar_beca(60.00)
class EstudianteCombinado(
    Estudiante,
    MatriculaExtemporanea,
    IndiceDesaprobatorio,
    BecaViolencia
):
    def calcular_total(self):
        monto =60.00
        monto +=self.cargo_matricula()
        monto +=self.cargo_indice()
        return self.aplicar_beca(monto)
#creamos objetos
estudiantes = [
    EstudianteCombinado("Luis Huamaní Cárdenas", 0),
    EstudianteCombinado("Rosa Ccahuana Prado", 0)
]

estudiantes[0].registrar_pago(45.00)
estudiantes[1].registrar_pago(45.00)

for estudiante in estudiantes:
    estudiante.mostrar_datos()
