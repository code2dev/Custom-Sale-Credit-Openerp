# -*- coding: utf-8 -*-
{
    'name': 'Personalizacion del Modulo de Venta',
    'version': '1.0.0',
    'category': 'Ventas',
    'sequence': 3,
    'author': 'Gerardo A Lopez Vega',
    'website': 'http://www.desiteg.com',
    'summary': "Permite customizar la vista de ventas",
    'description': "Permite customizar la vista de ventas mostrando el credito del cliente",
    'depends': ["sale"],
    'data': [        
        'mc_custom_sale_view.xml',
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
}