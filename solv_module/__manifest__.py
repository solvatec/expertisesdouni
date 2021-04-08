# -*- coding: utf-8 -*-
{
    'name': "solv_module",

    'summary': """
        solv_module""",

    'description': """
        solv_module
    """,

    'author': "OUASSIFOUH ABDELALI",
    'website': "www.solvatec.ma",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        # 'sale',
        # 'sale_management',
        # 'account',
        # 'hr',
    ],

    # always loaded
    'data': [
        #data
        'data/mail_notification_data.xml',
        'data/ir_sequence.xml',

        #security
        'security/ir.model.access.csv',
        'security/security.xml',

        #views
        'views/base/res_company_views.xml',
        'views/base/res_partner_views.xml',
        # 'views/sale/sale_order_views.xml',
        # 'views/account/invoice_views.xml',
        # 'views/hr/hr_employee_views.xml',
        # 'views/crm/crm_lead_views.xml',
        
        #wizards
        # 'wizard/wizard_add_product_view.xml',

        # reports
        # 'reports/sale_order_report.xml',
        # 'reports/invoice_report.xml',
        # 'reports/deliveryslip_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}