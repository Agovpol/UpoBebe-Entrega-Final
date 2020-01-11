# -*- coding: utf-8 -*-

from odoo import models, fields, api

class extras(models.Model):
    _name = 'upobebe.extras'

    name =  fields.Char('Nombre', size=70, required=True)
    descripcion = fields.Text('Descripcion')
    precio = fields.Float('Precio por unidad', size=6, required=True)
    id = fields.Char('ID', size=4, required=True)
    foto = fields.Binary('Foto') 
      
    articulo_ids = fields.Many2many("upobebe.articulo")
    numeroArticulos = fields.Integer(compute='_numeroArticulos', string='Nº artículos que tienen este extra', store=True) 
    
    @api.onchange('precio')
    def onchange_extras(self):
        resultado = {}
        if self.precio >= 101:
            resultado = {'value': {'precio' : 100 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Los extras no pueden estar valolados en más de 100 euros.'}}
        return resultado
    
    @api.one
    @api.depends('articulo_ids')
    def _numeroArticulos(self):                             
        self.numeroArticulos = len(self.articulo_ids)