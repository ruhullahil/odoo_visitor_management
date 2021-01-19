from odoo import models, fields, api, _


class VisitorExtersServices(models.Model):
    _name = 'visitor_management.extra_services'
    _description = 'check in extra services'

    service_selector = [('baggage', 'Baggage'), ('food', 'Food'), ('drinks', 'Drinks'), ('others', 'Others')]
    check_in_slot = fields.Many2one('visitor_management.visitor.checkincheckout', string='Check in')
    services = fields.Selection(service_selector, string="Services")
    cost = fields.Float(string='Cost')
    is_paid = fields.Boolean(string='is paid')
    remarks = fields.Char(string='Remarks')
