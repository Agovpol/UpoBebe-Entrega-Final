# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
    _name = 'upobebe.proveedor'

    name =  fields.Char('Nombre', size=60, required=True)
    nif = fields.Char('NIF', size=9, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    numero =  fields.Char('Telefono', size=9, required=True)
    correo = fields.Char('Correo', size=60, required=True)
    sede = fields.Selection([('sevilla','Sevilla'),('madrid','Madrid'),('barcelona','Barcelona'),('valencia','Valencia'),
                             ('bilbao','Bilbao'),('canarias','Canarias'),('asturias','Asturias')],
                                     'Sede')
    cp =  fields.Char('Codigo Postal', size=5, required=True)
    
    compra_ids = fields.Many2many('upobebe.compra', string='Compras de las que forma parte')
    numeroCompras = fields.Integer(compute='_numeroCompras', string='Nº compras de las que forma parte', store=True) 
    
    _sql_constraints = [('proveedor_nif_unique','UNIQUE (nif)','El NIF debe ser único.')]  
    
    @api.one
    @api.depends('compra_ids')
    def _numeroCompras(self):                             
        self.numeroCompras = len(self.compra_ids)