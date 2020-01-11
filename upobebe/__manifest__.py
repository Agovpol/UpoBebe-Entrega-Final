# -*- coding: utf-8 -*-
{
    'name': "upobebe",
    'summary': """Administracion UpoBebe""",
    'description': """Administracion UpoBebe:clases, usuarios, material...""",
    'author': "Grupo 9",
    'category': 'UpoBebe',
    'version': '0.1',
    'depends': ['base'],
    'data': ['views/venta_view.xml','views/cliente_view.xml','views/articulo_view.xml',
             'views/compra_view.xml','views/empleado_view.xml','views/proveedor_view.xml',
             'views/extras_view.xml','views/reparacion_view.xml','views/taller_view.xml'],
    'demo': ['demo/upobebe_demo.xml'],
    'application': True,
}
