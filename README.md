# Libreria del Centro

Este parcial trata de un sistema sencillo para calcular el precio final de productos con descuento e IVA.

## Particiones de equivalencia

Regla 1: el precio base debe ser mayor que cero.

| Regla | Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---|---|---|
| Regla 1 | precio base <= 0 | inválida | 0 | rechazar con mensaje claro |
| Regla 1 | precio base > 0 | válida | 100 | crear producto sin error |

Regla 2: el descuento debe estar entre 0% y 40%.

| Regla | Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---|---|---|
| Regla 2 | descuento < 0 | inválida | -1 | rechazar con mensaje claro |
| Regla 2 | descuento entre 0 y 40 | válida | 20 | aceptar el descuento |
| Regla 2 | descuento > 40 | inválida | 41 | rechazar con mensaje claro |

## Valores límite de la regla 2

| Valor | Esperado |
|---|---|
| -1 | inválido |
| 0 | válido |
| 1 | válido |
| 39 | válido |
| 40 | válido |
| 41 | inválido |

## Pregunta para la regla 3

¿El precio final se redondea a dos decimales o se deja con más precisión? Eso cambia cómo se validan los resultados.

## Casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | Regla 1 | crear producto con precio válido | no existe producto | nombre libro, precio 100 | crear producto | se crea sin error | Positivo |
| CP-02 | Regla 1 | rechazar precio base cero | no existe producto | nombre libro, precio 0 | crear producto | lanza error | Negativo |
| CP-03 | Regla 1 | rechazar precio base negativo | no existe producto | nombre libro, precio -5 | crear producto | lanza error | Negativo |
| CP-04 | Regla 2 | aceptar descuento de cero | producto creado | descuento 0 | aplicar descuento | se acepta el valor | Borde |
| CP-05 | Regla 2 | aceptar descuento en el máximo | producto creado | descuento 40 | aplicar descuento | se acepta el valor | Borde |
| CP-06 | Regla 2 | rechazar descuento arriba del límite | producto creado | descuento 41 | aplicar descuento | lanza error | Negativo |
| CP-07 | Regla 3 | calcular precio con descuento medio | producto creado con descuento 20 | precio base 100 | calcular precio final | devuelve 95.20 | Positivo |
| CP-08 | Regla 3 | calcular precio sin descuento | producto creado | precio base 100, descuento 0 | calcular precio final | devuelve 119.00 | Positivo |

## Cobertura

La suite de pruebas me dio 100% de cobertura en el módulo principal.

| Archivo | Stmts | Miss | Cover |
|---|---|---|---|
| src/libreria_parcial/__init__.py | 1 | 0 | 100% |
| src/libreria_parcial/producto.py | 21 | 0 | 100% |
| TOTAL | 22 | 0 | 100% |