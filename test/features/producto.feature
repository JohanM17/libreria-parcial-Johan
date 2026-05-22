Feature: Calculo de precio en la libreria
  Como administrador de la libreria
  Quiero calcular descuentos e IVA en los productos
  Para saber el precio final correcto antes de vender.

  Background:
    Given un producto llamado "Libro" con precio base de 100

  @descuento @positivo
  Scenario: aplicar descuento de cero por ciento
    When aplico un descuento de 0 por ciento
    Then el precio final deberia ser 119.00

  @descuento @limite
  Scenario: aplicar descuento de cuarenta por ciento
    When aplico un descuento de 40 por ciento
    Then el precio final deberia ser 71.40

  @descuento @error
  Scenario: rechazar descuento mayor al permitido
    When intento aplicar un descuento de 41 por ciento
    Then deberia salir un error con el mensaje "El descuento debe estar entre 0% y 40%"

  @precio @positivo
  Scenario Outline: calcular precio final con descuentos validos
    When aplico un descuento de <descuento> por ciento
    Then el precio final deberia ser <precio>

    Examples:
      | descuento | precio |
      | 10        | 107.10 |
      | 20        | 95.20  |

  @precio @positivo
  Scenario: calcular precio final sin descuento
    When no aplico descuento
    Then el precio final deberia ser 119.00