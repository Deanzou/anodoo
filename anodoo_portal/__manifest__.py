# -*- coding: utf-8 -*-
{
    'name': "客户门户",

    'summary': """
        客户门户
    """,

    'description': """
        客户门户
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-portal",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['portal',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/portal_data.xml',
        #'demo/demo.xml',#demo
        'security/portal_security.xml',
        'security/ir.model.access.csv',
        'views/portal_views.xml',
        'views/res_config_settings_views.xml',
        'views/portal_menu.xml',
        'views/portal_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}