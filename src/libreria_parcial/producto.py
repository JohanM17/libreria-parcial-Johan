from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


IVA = Decimal("0.19")


@dataclass
class Producto:
    nombre: str
    precio_base: Decimal | float | int
    descuento: Decimal = field(default=Decimal("0"), init=False)

    def __post_init__(self):
        self.precio_base = Decimal(str(self.precio_base))
        if self.precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

    def aplicar_descuento(self, porcentaje: Decimal | float | int):
        porcentaje = Decimal(str(porcentaje))
        if porcentaje < 0 or porcentaje > 40:
            raise ValueError("El descuento debe estar entre 0% y 40%")
        self.descuento = porcentaje

    def calcular_precio_final(self):
        subtotal = self.precio_base * (Decimal("1") - (self.descuento / Decimal("100")))
        total = subtotal * (Decimal("1") + IVA)
        return max(Decimal("0"), total).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)