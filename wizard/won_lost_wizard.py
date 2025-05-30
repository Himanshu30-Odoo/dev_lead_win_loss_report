# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields,api,_
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class WonLostWizard(models.TransientModel):
    _name = 'won.lost'
    _description = 'CRM Won Lost Lead Wizard'

    start_date = fields.Date(string='Start Date',default=fields.Datetime.today(), required=True)
    end_date = fields.Date(string='End Date',required=True)
    user_ids = fields.Many2many('res.users', string='Salespersons')
    
    
    @api.onchange('end_date','start_date')  
    def onchange_of_end_date(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                    raise ValidationError(_("End date must be greater than the start date."))


    def print_crm_lead_report(self):
        return self.env.ref('dev_lead_win_loss_report.won_lost_report_menu').report_action(self)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
