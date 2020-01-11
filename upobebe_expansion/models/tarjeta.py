# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tarjeta(models.Model):
    _name = 'upobebe_expansion.tarjeta'

    name = fields.Char('Nombre tarjeta', size=64, required=True)
    cantidad = fields.Integer('Cantidad')
    materialType = fields.Selection([('descuento','Descuento'),
                                     ('dinero','Dinero'),
                                     ('otro','Otro'),],
                                     'Tipo de tarjeta')
    cliente_ids = fields.Many2many("upobebe.cliente",string="Clientes con tarjetas")
    venta_ids =  fields.Many2many('upobebe.venta',string='Ventas') 
