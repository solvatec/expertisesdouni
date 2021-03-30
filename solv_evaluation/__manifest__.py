# -*- coding: utf-8 -*-
{
    'name': "solv_evaluation",

    'summary': """
        solv_evaluation""",

    'description': """
        ajout des champs dans le module projet
    """,

    'author': "solvatec",
    'website': "http://www.solvatec.ma",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'project',
    ],

    # always loaded
    'data': [
        #data
        # security
        'security/ir.model.access.csv',
        'security/security.xml',
        #views
        'views/evaluation/evaluation_views.xml',
        'views/evaluation/project_stage_views.xml',
        #menu
        'menu/menu.xml',
        #wizards
        # 'wizard/wizard_add_product_view.xml',
        # reports
        # 'reports/fleet_order_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'css': [
        'static/src/css/project.css',
    ],
    'scss': [
        'static/src/scss/portal_rating.scss',
        'static/src/scss/project_dashboard.scss',
    ],
    'js': [
        'static/src/js/project_kanban.js',
    ],
}