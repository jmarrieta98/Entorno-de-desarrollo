#!/usr/bin/python
#-*- coding: utf-8 -*-

from Alumno import Alumno

class Personas(Alumno):
    def __init__(self):
        self.Nombre = None
        self.Correo = None
        self.Direccion = None
        self.Telefono = None
        self.Alias = None

