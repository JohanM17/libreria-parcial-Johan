análisis inicial

regla 1 y regla 2

particiones de equivalencia

| Regla | Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---|---|---|
| Regla 1 | precio base menor o igual a 0 | inválida | 0 | rechazar con mensaje claro |
| Regla 1 | precio base mayor a 0 | válida | 100 | crear producto sin error |
| Regla 2 | descuento menor a 0 | inválida | -1 | rechazar con mensaje claro |
| Regla 2 | descuento entre 0 y 40 | válida | 20 | aceptar el descuento |
| Regla 2 | descuento mayor a 40 | inválida | 41 | rechazar con mensaje claro |

análisis de valores límite para la regla 2

| Valor | Esperado |
|---|---|
| -1 | inválido |
| 0 | válido |
| 1 | válido |
| 39 | válido |
| 40 | válido |
| 41 | inválido |

pregunta para el administrador sobre la regla 3

¿el precio final debe redondearse a dos decimales o se deja con más precisión, porque eso cambia la forma de validar los resultados?

casos de prueba

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

reporte de cobertura

=============================== tests coverage ================================
_______________ coverage: platform win32, python 3.12.9-final-0 _______________

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
src\libreria_parcial\__init__.py       1      0   100%
src\libreria_parcial\producto.py      21      0   100%
----------------------------------------------------------------
TOTAL                                 22      0   100%