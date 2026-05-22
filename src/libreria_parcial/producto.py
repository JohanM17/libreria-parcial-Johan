from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


IVA = Decimal("0.19")


@dataclass
class Producto:
    nombre: str
    precio_base: Decimal | float | int
    descuento: Decimal = field(default=Decimal("0"), init=False)

    def __post_init__(self):
        self.precio_base = self._a_decimal(self.precio_base)
        self._validar_precio_base()

    def aplicar_descuento(self, porcentaje: Decimal | float | int):
        porcentaje_decimal = self._a_decimal(porcentaje)
        self._validar_descuento(porcentaje_decimal)
        self.descuento = porcentaje_decimal

    def calcular_precio_final(self) -> Decimal:
        subtotal = self._calcular_subtotal_con_descuento()
        total = subtotal * (Decimal("1") + IVA)
        return max(Decimal("0"), total).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def _a_decimal(self, valor: Decimal | float | int) -> Decimal:
        return Decimal(str(valor))

    def _validar_precio_base(self):
        if self.precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

    def _validar_descuento(self, porcentaje: Decimal):
        if porcentaje < 0 or porcentaje > 40:
            raise ValueError("El descuento debe estar entre 0% y 40%")

    def _calcular_subtotal_con_descuento(self) -> Decimal:
        return self.precio_base * (Decimal("1") - (self.descuento / Decimal("100")))