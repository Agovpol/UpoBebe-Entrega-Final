# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'upobebe.cliente'

    name =  fields.Char('Nombre', size=60, required=True)
    apellidos =  fields.Char('Apellidos', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    numero =  fields.Char('Telefono', size=9, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    correo = fields.Char('Correo', size=60, required=True)
    cp =  fields.Char('Codigo Postal', size=5, required=True)
    
    venta_ids = fields.One2many('upobebe.venta','cliente_id', 'Ventas')
    numeroVentas = fields.Integer(compute='_numeroVentas', string='Nº compras realizadas', store=True) 
    
    _sql_constraints = [('cliente_dni_unique','UNIQUE (dni)','El DNI debe ser único.')]
    
    @api.one
    @api.depends('venta_ids')
    def _numeroVentas(self):                             
        self.numeroVentas = len(self.venta_ids)
