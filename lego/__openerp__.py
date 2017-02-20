# -*- coding: utf-8 -*-
{
    'name': "lego",

    'summary': """Lego club""",
    
    'description': """
        Lego
    """,

    'icon': "/lego/static/img/lego.png",

    'author': "Jaime Lopez Viartola",
    'website': "http://viartolasalesiano.blogspot.com.es/2012_12_01_archive.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rubrica',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
