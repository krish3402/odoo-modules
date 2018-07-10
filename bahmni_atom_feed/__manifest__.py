# -*- coding: utf-8 -*-
{
    'name': 'Bahmni Atom Feed',
    'version': '1.0',
    'summary': 'Module to sync Bahmni with Odoo',
    'sequence': 1,
    'description': """
Bahmni Web Extension
====================
""",
    'category': 'Web',
    'website': '',
    'images': [],
    'depends': ['web', 'bahmni_product', 'bahmni_sale'],
    'data': ['views/event_records_view.xml',
             'views/res_partner_view.xml',
             'views/res_company.xml',
             'wizard/stock_location_product_dhis2.xml',
             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
