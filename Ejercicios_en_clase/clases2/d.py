# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:15:36 2022

@author: Juan Carlos
"""

import c

class UsuariosPremiumPlus(c.UsuariosPremium):
	participacion_sorteos = 25

	def muestra_datos(self):
		super().muestra_datos()
		print("El tipo de usuario es: ", c.UsuariosPremium.tipo_usuario)