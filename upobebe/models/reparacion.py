# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reparacion(models.Model):
    _name = 'upobebe.reparacion'

    id = fields.Char('ID', size=4, required=True)
    name =  fields.Char('Nombre', size=70, required=True)
    descripcion = fields.Text('Descripcion')
    precio = fields.Float('Precio por unidad', size=6, required=True)
    fecha = fields.Date('Fecha de la reparación',required=True, autodate = True)
    tipo = fields.Selection([('completa','Completa'),('pintura','Pintura'),('accesorios','Accesorios'),('recambio','Recambio')]
                           , 'Tipo de reparación')
    state = fields.Selection([('pendiente','Pendiente de reparación'),('recopilar','Recopilando'),
                                     ('comenzar','Reparación en curso'),('reparado','Reparado'),],
                                     'Estado', default='pendiente')
    
    venta_ids = fields.Many2many('upobebe.venta', string="Ventas relacionadas")   
    taller_id =  fields.Many2one("upobebe.taller",string="Taller")
    numeroVentas = fields.Integer(compute='_numeroVentas', string='Nº ventas que incluyen esta reparación', store=True)
    
    @api.one
    def btn_submit_to_recopilar(self):
        self.write({'state':'recopilar'})
        
    @api.one
    def btn_submit_to_comenzar(self):
        self.write({'state':'comenzar'})
        
    @api.one
    def btn_submit_to_reparado(self):
        self.write({'state':'reparado'})

    @api.onchange('precio','tipo')
    def onchange_reparacion(self):
        resultado = {}
        if self.precio >= 51 and (self.tipo == 'accesorios' or self.tipo == 'pintura'):
            resultado = {'value': {'precio' : 50 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Las reparaciones de accesorios y pintura no pueden estar valoradas en más de 50 euros.'}}
        return resultado
    
    @api.one
    @api.depends('venta_ids')
    def _numeroVentas(self):                             
        self.numeroVentas = len(self.venta_ids)