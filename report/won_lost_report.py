
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
from odoo import models, fields, api
import itertools
import operator

class WonLostReport(models.AbstractModel):
    _name = 'report.dev_lead_win_loss_report.won_lost_template1'
    _description = 'Won Lost Lead Report'

    def wonlost_history(self, obj):
        domain = [
            ('create_date', '>=', obj.start_date), 
            ('create_date', '<=', obj.end_date),
            ('type','=','opportunity')
        ]

        if obj.user_ids:
            domain.append(('user_id', 'in', obj.user_ids.ids))

        won_domain = domain + [('active', '=', True), ('stage_id.is_won', '=', True)]
        won_leads = self.env['crm.lead'].search(won_domain)

        lost_domain = domain + [('active', '=', False), ('probability', '=', 0)]
        lost_leads = self.env['crm.lead'].search(lost_domain)

        data = []

        # Group by User
        users = set(won_leads.mapped('user_id.id') + lost_leads.mapped('user_id.id'))
        for user_id in users:
            user = self.env['res.users'].browse(user_id)
            user_data = {
                'user_name': user.name or "No User",
                'won': [],
                'lost': []
            }

            for lead in won_leads.filtered(lambda l: l.user_id.id == user_id):
                user_data['won'].append({
                    'name': lead.name,
                    'partner_name': lead.partner_id.name or "No Partner",
                    'stage_name': lead.stage_id.name,
                    'expected_closing': lead.date_deadline,
                })

            for lead in lost_leads.filtered(lambda l: l.user_id.id == user_id):
                user_data['lost'].append({
                    'name': lead.name,
                    'partner_name': lead.partner_id.name or "No Partner",
                    'stage_name': lead.stage_id.name,
                    'expected_closing': lead.date_deadline,
                })

            data.append(user_data)

        return data

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['won.lost'].browse(docids)
        wonlost_history = self.wonlost_history(docs[0])
        return {
            'doc_ids': docs.ids,
            'doc_model':'won.lost',
            'docs': docs,
            'wonlost_history': wonlost_history,
        }
