# -*- coding: utf-8 -*-
{
    'name': 'ALLSS - WATERMARK - QUOTATION',
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
        'base',
        'web',
        'product',
        'sale_management'
    ],
    'data': [
        #view
        'views/res_company_views.xml',
        'views/sale_order_custom.xml',
        'report/template_contract_allss.xml',

        #report
        'report/external_layout_template.xml',
    ],
    'images': [
        'static/description/ALLLSS Soluções em Sistemas.png',
    ],
    'auto_install': False,
    'installable': True,
    'application': False
}
