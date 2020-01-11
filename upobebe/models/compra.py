# -*- coding: utf-8 -*-

from odoo import models, fields, api

class compra(models.Model):
    _name = 'upobebe.compra'

    id = fields.Char('ID', size=4, required=True)
    importe = fields.Float('Importe', size=6, required=True)
    fecha = fields.Date('Fecha', required=True, autodate=True)
    comentarios = fields.Text('Comentarios')
    state = fields.Selection([('pendiente','Pendiente de envío'),('envio','En proceso de envío'),
                                     ('entregado','Entregado'),],
                                     'Estado', default='pendiente')
    
    empleado_id =  fields.Many2one("upobebe.empleado",string="Empleado")
    proveedor_ids = fields.Many2many("upobebe.proveedor")
    articulo_ids = fields.Many2many("upobebe.articulo")
    numeroArticulos = fields.Integer(compute='_numeroArticulos', string='Nº artículos', store=True) 
    numeroProveedor = fields.Integer(compute='_numeroProveedor', string='Nº proveedores', store=True)
    
    @api.one
    def btn_submit_to_enviado(self):
        self.write({'state':'envio'})
        
    @api.one
    def btn_submit_to_entregado(self):
        self.write({'state':'entregado'}) 
    
    @api.one
    @api.depends('articulo_ids')
    def _numeroArticulos(self):                             
        self.numeroArticulos = len(self.articulo_ids)
        
    @api.one
    @api.depends('proveedor_ids')
    def _numeroProveedor(self):                             
        self.numeroProveedor = len(self.proveedor_ids)

    
    