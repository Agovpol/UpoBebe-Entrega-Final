# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
 
    _inherit = 'upobebe.cliente'
    
    tarjeta_ids =  fields.Many2many('upobebe_expansion.tarjeta',string="Tarjetas regalo")