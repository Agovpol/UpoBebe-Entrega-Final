# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upobebe.venta'

    id = fields.Char('ID', size=4, required=True)
    importe = fields.Float('Importe', size=6, required=True)
    fecha = fields.Date('Fecha', required=True, autodate=True)
    comentarios = fields.Text('Comentarios')
    state = fields.Selection([('pendiente','Pendiente de envío'),('envio','En proceso de envío'),
                                     ('entregado','Entregado'),],
                                     'Estado', default='pendiente')
    
    cliente_id =  fields.Many2one("upobebe.cliente",string="Cliente")
    articulo_ids = fields.Many2many("upobebe.articulo")
    reparacion_ids = fields.Many2many("upobebe.reparacion")
    numeroArticulos = fields.Integer(compute='_numeroArticulos', string='Nº artículos', store=True) 
    numeroReparaciones = fields.Integer(compute='_numeroReparaciones', string='Nº reparaciones', store=True) 

    @api.one
    def btn_submit_to_enviado(self):
        self.write({'state':'envio'})
        
    @api.one
    def btn_submit_to_entregado(self):
        self.write({'state':'entregado'})
        
    @api.onchange('reparacion_ids')
    def onchange_reparacion(self):
        if self.state != 'entregado':
            raise models.ValidationError('La venta debe haber sido entregada para poder ser enviada a la reparación.')
        
    @api.one
    @api.depends('articulo_ids')
    def _numeroArticulos(self):                             
        self.numeroArticulos = len(self.articulo_ids)
        
    @api.one
    @api.depends('reparacion_ids')
    def _numeroReparaciones(self):                             
        self.numeroReparaciones = len(self.reparacion_ids)


