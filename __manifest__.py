
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
{
    'name': 'Won lost report',
    'version': '17.0.1.2',
    'sequence': 1,
    'category': 'Crm',
    'description':
        """

       Won lost report\n

    """,
    'summary': 'Won lost report',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['crm','base'],
    'data': [
    	'security/ir.model.access.csv',
    	'wizard/won_lost_wizard.xml',
        'report/won_lost_report.xml',
        'report/report_menu.xml',

    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
