from decimal import Decimal

import pytest

from libreria_parcial.producto import Producto


def test_no_deberia_crear_producto_con_precio_base_cero():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", 0)


def test_no_deberia_crear_producto_con_precio_base_negativo():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Libro", -5)


def test_deberia_permitir_descuento_cero():
    producto = Producto("Libro", 100)
    producto.aplicar_descuento(0)
    assert producto.descuento == Decimal("0")


def test_no_deberia_permitir_descuento_mayor_a_cuarenta():
    producto = Producto("Libro", 100)
    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(41)


def test_precio_final_deberia_aplicar_descuento_e_iva():
    producto = Producto("Libro", 100)
    producto.aplicar_descuento(10)
    assert producto.calcular_precio_final() == Decimal("107.10")


def test_precio_final_sin_descuento_deberia_incluir_iva():
    producto = Producto("Libro", 100)
    assert producto.calcular_precio_final() == Decimal("119.00")


def test_descuento_en_el_limite_superior_deberia_funcionar():
    producto = Producto("Libro", 100)
    producto.aplicar_descuento(40)
    assert producto.calcular_precio_final() == Decimal("71.40")


def test_descuento_en_el_limite_inferior_deberia_funcionar():
    producto = Producto("Libro", 100)
    producto.aplicar_descuento(0)
    assert producto.calcular_precio_final() == Decimal("119.00")