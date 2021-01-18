# -*- coding: utf-8 -*-
{
    'name': "visitor_management",

    'summary': """
        this is use for managing visitor , it also use to mange how many use is enter every day. who is enter when enter when out 
         and many other thing """,

    'description': """
        this is not fully discribed yet
    """,

    'author': "Ruhullahil kabir",
    'website': "http://www.uslbd.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',],

    # always loaded
    'data': [

        'security/security.xml',
        'report/visitor_id_card.xml',
        'report/report.xml',
        'report/all_employee_report.xml',
        'report/all_visitor_report.xml',
        'report/indevisual_employee_report_with_start_end_date.xml',
        'report/indevisual_visitor_report_with_start_end_date.xml',
        'views/visitor.xml',
        'views/employee.xml',
        'views/employee_booked.xml',
        'views/employee_time_slot.xml',
        'views/employee_checkout.xml',
        'views/employee_checkin.xml',
        'views/visitor_checkin.xml',
        'views/visitor_checkour.xml',
        'wizards/employee_report.xml',
        'wizards/visitor_report.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'data/visitor_corn.xml'
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


    'installable': True,
    'application': True,
    'auto_install': False,
}
