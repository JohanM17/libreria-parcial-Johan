from decimal import Decimal

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from libreria_parcial.producto import Producto


scenarios("../features/producto.feature")


@given(parsers.parse('un producto llamado "{nombre}" con precio base de {precio_base}'), target_fixture="producto")
def producto(nombre, precio_base):
    return Producto(nombre, Decimal(precio_base))


@when(parsers.parse("aplico un descuento de {descuento} por ciento"))
def aplicar_descuento(producto, descuento):
    producto.aplicar_descuento(Decimal(descuento))


@when(parsers.parse("intento aplicar un descuento de {descuento} por ciento"), target_fixture="error")
def intentar_aplicar_descuento(producto, descuento):
    try:
        producto.aplicar_descuento(Decimal(descuento))
    except ValueError as error:
        return error
    return None


@when("no aplico descuento")
def no_aplico_descuento(producto):
    producto.aplicar_descuento(0)


@then(parsers.parse("el precio final deberia ser {precio}"))
def precio_final(producto, precio):
    assert producto.calcular_precio_final() == Decimal(precio)


@then(parsers.parse('deberia salir un error con el mensaje "{mensaje}"'))
def error_descuento(error, mensaje):
    assert isinstance(error, ValueError)
    assert str(error) == mensaje