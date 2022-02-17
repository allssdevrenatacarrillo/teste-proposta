# -*- coding: utf-8 -*-
{
    'name': 'ALLSS - Dynamic Sale Order Quotation ALLSS',
    'version': '14.0.1.0.0',
    'licence':'AGPL-3',
    'category': 'Sale',
    'author': 'ALLSS Soluções em Sistemas',
    'company': 'ALLSS Soluções em Sistemas',
    'website': 'https://allss.com.br',
    'summary': 'Dynamic Sale Order Quotation - ALLSS Soluções em Sistemas',
    'description':'Dynamic Sale Order Quotation - by ALLSS Soluções em Sistemas',
    'contributors': [
        'Nathan Oliveira (nathan.oliveira@allss.com.br)',
        'Anderson Coelho (anderson.coelho@allss.com.br)',
        'Renata Carrillo (renata.carrillo@allss.com.br)',
    ],
    'depends': [
        'sale',
        'web',
        'sale_management'
    ],
    'data': [
        # report
        'report/view_custom_contract.xml',
        'report/view_custom_portal.xml',
        'report/view_custom_quotation.xml',

        # views
        'views/sale_order_tml_custom.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
