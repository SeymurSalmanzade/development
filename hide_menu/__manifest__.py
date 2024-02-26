# -*- coding: utf-8 -*-
{
    'name': "hide_menu",

    'summary': """Restrict Menu Items from Specific Users""",

    'description': """
Restrict Menu Items from Specific Users
    """,

    'author': "ERPGO",
    'website': "https://www.erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Rights',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

