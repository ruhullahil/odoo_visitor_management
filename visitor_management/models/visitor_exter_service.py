from odoo import models, fields, api, _


class VisitorExtersServices(models.Model):
    _name = 'visitor_management.extra_services'
    _description = 'check in extra services'

    baggage_type_selector = [('big', 'Big'), ('small', 'Small'), ('others', 'Others')]
    check_in_slot = fields.Many2one('visitor_management.visitor.checkincheckout', string='Check in')
    have_any_baggage = fields.Boolean(string='Baggage ', default=False)
    baggage_type = fields.Selection(baggage_type_selector, default='small', string='Baggage Type')
    baggage_store_token = fields.Char(string='Baggage Token')
    want_lunch = fields.Boolean(string='Lunch', default=False)
