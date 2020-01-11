# -*- coding: utf-8 -*-

from odoo import models, fields, api

class articulo(models.Model):
    _name = 'upobebe.articulo'

    name =  fields.Char('Nombre', size=70, required=True)
    precio = fields.Float('Precio por unidad', size=6, required=True)
    foto = fields.Binary('Foto') 
    descripcion = fields.Text('Descripcion')
    id = fields.Char('ID', size=4, required=True)
    
    venta_ids = fields.Many2many('upobebe.venta', string='Ventas de las que forma parte')  
    compra_ids = fields.Many2many('upobebe.compra', string='Compras de las que forma parte')  
    extras_ids = fields.Many2many('upobebe.extras', string='EXTRAS')  
    numeroCompras = fields.Integer(compute='_numeroCompras', string='Nº compras', store=True) 
    numeroExtras = fields.Integer(compute='_numeroExtras', string='Nº extras', store=True) 
    numeroVentas = fields.Integer(compute='_numeroVentas', string='Nº ventas', store=True)
    
    @api.one
    @api.depends('compra_ids')
    def _numeroCompras(self):                             
        self.numeroCompras = len(self.compra_ids)
        
    @api.one
    @api.depends('extras_ids')
    def _numeroExtras(self):                             
        self.numeroExtras = len(self.extras_ids)
        
    @api.one
    @api.depends('venta_ids')
    def _numeroVentas(self):                             
        self.numeroVentas = len(self.venta_ids)
        
    def eliminarVentas(self):         
        # Eliminamos los registros de la relación many2many 
        self.write({'venta_ids':[ (5,  ) ]})  
        
    def eliminarCompras(self):         
        # Eliminamos los registros de la relación many2many 
        self.write({'compra_ids':[ (5,  ) ]})
        
    def eliminarExtras(self):         
        # Eliminamos los registros de la relación many2many 
        self.write({'extras_ids':[ (5,  ) ]})
    
    
    
    
