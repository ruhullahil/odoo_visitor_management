from odoo import models, fields, api, _


class VisitorProfile(models.Model):
    _name = 'visitor_management.visitor'
    _description = 'visitor profile is model where store all info  of any visitor ever visit'
    _rec_name = 'visitor_name'

    @api.model
    def create(self, vals):
        print("------------ : create called")
        if vals.get('visitor_seq', _('New')) == _('New'):
            vals['visitor_seq'] = self.env['ir.sequence'].next_by_code('visitor_management.visitor') or _('New')
        result = super(VisitorProfile, self).create(vals)
        print(result)
        return result

    visitor_name = fields.Char(string="Visitor Name ", required=True)
    phone_number = fields.Char(string='Phone Number', required=True, size=14)
    address = fields.Char(string="Address", required=True)
    email = fields.Char(string='Email')
    visitor_seq = fields.Char(string='visitor sequence', required=True, copy=False, readonly=False,
                              index=True, default=lambda self: _('New'))
    image = fields.Binary(string="Image", attachment=True)
