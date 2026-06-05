Feature: Recargas telefonicas

Scenario: Recarga valida sin bonificacion
  Given un usuario normal
  When realiza una recarga de 5000
  Then recibe 0 por ciento de bonificacion

Scenario: Recarga de 10000
  Given un usuario normal
  When realiza una recarga de 10000
  Then recibe 10 por ciento de bonificacion

Scenario: Recarga de 30000
  Given un usuario normal
  When realiza una recarga de 30000
  Then recibe 25 por ciento de bonificacion

Scenario: Usuario premium
  Given un usuario premium
  When realiza una recarga de 30000
  Then recibe 30 por ciento de bonificacion

Scenario Outline: Validacion de montos

  Given un usuario
  When realiza una recarga de <monto>
  Then la recarga es <resultado>

Examples:
  | monto | resultado |
  | 999 | rechazada |
  | 1000 | aprobada |
  | 50000 | aprobada |
  | 50001 | rechazada |