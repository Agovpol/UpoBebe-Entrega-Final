# -*- coding: utf-8 -*-
from odoo import http

# class UpobebeExpansion(http.Controller):
#     @http.route('/upobebe_expansion/upobebe_expansion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upobebe_expansion/upobebe_expansion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upobebe_expansion.listing', {
#             'root': '/upobebe_expansion/upobebe_expansion',
#             'objects': http.request.env['upobebe_expansion.upobebe_expansion'].search([]),
#         })

#     @http.route('/upobebe_expansion/upobebe_expansion/objects/<model("upobebe_expansion.upobebe_expansion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upobebe_expansion.object', {
#             'object': obj
#         })