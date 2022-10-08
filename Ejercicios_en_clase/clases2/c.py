# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:15:20 2022

@author: Juan Carlos
"""

import b

class UsuariosPremium(b.Usuarios):
    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios):
        self.participacion_sorteos = participacion_sorteos
        self.puntos_premios = puntos_premios
        self.contenido_premium = True
        super().__init__(nid, alias, nombre, apellidos)

    def muestra_datos(self):
        super().muestra_datos()
        print("Tienes ", self.puntos_premios, " puntos para canjear en premios.")
        print("Tienes ", self.participacion_sorteos, " puntos para participar en sorteos.")

    tipo_usuario = "Premium"
    publicidad = False
    participacion_sorteos = 10