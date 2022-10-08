# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:14:20 2022

@author: Juan Carlos
"""

import b
import c
import d

def muestra_datos_comun(self):
	print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
	print("El ID de usuario es: " + self.nid + ".")
	print("El alias del usuario es: " + self.alias + ".")


usuario1=b.Usuarios("001", "raulito43", "Raúl", "Fernández Gomila")

usuario2=c.UsuariosPremium("002", "PdePython", "Paula", "Vega García",  10, 500)

usuario3=d.UsuariosPremiumPlus("003", "BreakTheSystem", "Anonymous", "Anonymous Anonymous", 25, 1500)

print("\nDATOS USUARIO 1 - Usuarios")
usuario1.muestra_datos()
print("\nDATOS USUARIO 2 - UsuariosPremium")
usuario2.muestra_datos()
print("\nDATOS USUARIO 3 - UsuariosPremiumPlus")
usuario3.muestra_datos()