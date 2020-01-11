# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empleado(models.Model):
    _name = 'upobebe.empleado'

    id = fields.Char('DNI', size=9, required=True)
    name =  fields.Char('Nombre', size=60, required=True)
    apellidos =  fields.Char('Apellidos', size=60, required=True)
    salario = fields.Float('Salario', size=6, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    correo = fields.Char('Correo', size=60, required=True)
    rol = fields.Selection([('director','Director'),('subdirector','Subdirector'),('rrhh','RRHH'),('contable','Contable'),
                            ('dependiente','Dependiente'),('jefetienda','Jefe de tienda'),('becario','Becario'),('ejecutivo','Ejecutivo')],'Rol')
    numero =  fields.Char('Telefono', size=9, required=True)
    fechaini = fields.Date('Fecha inicio contrato', required=True, autodate=True)
    cp =  fields.Char('Codigo Postal', size=5, required=True)
    fechafin = fields.Date('Fecha final contrato', required=True, autodate=True)
    
    compra_ids = fields.One2many('upobebe.compra','empleado_id', 'Compras')
    numeroCompras = fields.Integer(compute='_numeroCompras', string='Nº compras', store=True) 
    
    @api.one
    @api.depends('compra_ids')
    def _numeroCompras(self):                             
        self.numeroCompras = len(self.compra_ids)
        
    @api.one
    @api.constrains('salario')
    def _check_salario(self):
        if self.salario<= 599:
            raise models.ValidationError('El salario debe ser superior como mínimo de 600 euros.')
        
    def eliminarCompras(self):         
        # Eliminamos los registros de la relación one2many 
        self.write({'compra_ids':[ (5,  ) ]})
