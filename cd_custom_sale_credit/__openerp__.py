# -*- coding: utf-8 -*-
{
    'name': 'Personalizacion del Modulo de Venta',
    'version': '1.0.0',
    'category': 'Ventas',
    'sequence': 3,
    'author': 'Gerardo A Lopez Vega @glopzvega',
    'website': 'http://www.codetodev.com',
    'summary': "Permite customizar la vista de ventas",
    'description': "Permite customizar la vista de ventas mostrando el credito del cliente",
    'depends': ["sale"],
    'data': [        
        'cd_custom_sale_credit_view.xml',
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
}