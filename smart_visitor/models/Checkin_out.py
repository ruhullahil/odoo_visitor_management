from odoo import models, fields, api


class VisitorCheckInOut(models.Model):
    _name = 'visitor.check.in.out'
    _rec_name = 'phone'

    # @api.depends('is_internal')
    # def show_visitor(self):
    #     for rec in self:
    #         print('bbbbb')
    #         if rec.is_internal:
    #             rec.visitor_name = self.env['smart_visitor'].search([('is_internal', '=', True)])
    #         rec.visitor_name = self.env['smart_visitor'].search([('is_internal', '=', False)])

    is_internal = fields.Boolean(string='Internal', )
    visitor_name = fields.Many2one('smart_visitor', string='Visitor Name',domain="[('is_internal','=',is_internal)]")
    email = fields.Char(related='visitor_name.email', string='Email')
    phone = fields.Char(related='visitor_name.phone_number', string='Phone')
    come_from = fields.Char(string='Come From')
    purpose = fields.Text(strig='Purpose')
    check_in_time = fields.Datetime(string="Check in Time")
    check_out_time = fields.Datetime(string="Check out Time")
    image = fields.Binary(string="Image", attachment=True)
    check_in_status = fields.Boolean(string='Check In Status')
    visitor_booked = fields.One2many('booked.schedule', 'visitor_id', string="Visitor")
