# -*- coding: utf-8 -*-
# Email: sales@creyox.com
{
    'name': 'Mass Cancel(Sales, Purchases, Invoices) | Mass Cancel Orders',
    "author": "Creyox Technologies",
    'category': 'Extra Tools',
    'sequence': '1',
    'version': '17.0',
    'price': 0,
    'currency': 'USD',
    'summary': "It helps to cancel multiple orders at a time.",
    'description':
        """Mass cancel the orders.""",
    "license": "LGPL-3",
    'depends': ['base', 'sale_management', 'purchase', 'account'],
    'data': [
        'security/groups.xml',
        'views/mass_cancel_action.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
