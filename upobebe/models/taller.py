# -*- coding: utf-8 -*-

from odoo import models, fields, api

class taller(models.Model):
    _name = 'upobebe.taller'

    name =  fields.Char('Nombre', size=70, required=True)
    nif = fields.Char('NIF', size=9, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    cp =  fields.Char('Codigo Postal', size=5, required=True)
    numero =  fields.Char('Telefono', size=9, required=True)
    
    reparacion_ids = fields.One2many('upobebe.reparacion','taller_id', 'Reparaciones')
    numeroReparaciones = fields.Integer(compute='_numeroReparaciones', string='Nº reparaciones que realiza', store=True)
    
    _sql_constraints = [('taller_nif_unique','UNIQUE (nif)','El NIF debe ser único.')]  
    
    @api.one
    @api.depends('reparacion_ids')
    def _numeroReparaciones(self):                             
        self.numeroReparaciones = len(self.reparacion_ids)
        
    def eliminarReparaciones(self):         
        # Eliminamos los registros de la relación one2many 
        self.write({'reparacion_ids':[ (5,  ) ]})