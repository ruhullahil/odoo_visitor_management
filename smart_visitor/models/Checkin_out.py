from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError


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
    @api.model
    def create(self, vals_list):
        # print(vals_list)
        # resource_type is 'human' by default. As we are not living in
        # /r/latestagecapitalism, workcenters are 'material'

        if not vals_list['check_in_time']:
            print('come here')
            vals_list['check_in_time'] = datetime.datetime.now()
            vals_list['check_in_status'] = True

        print(vals_list)
        print(vals_list['visitor_booked'][0][2])
        booked_list = self.env['booked.schedule'].search(
            ['&', '|', '&', ('start_time', '>=', vals_list['visitor_booked'][0][2]['start_time']), (
                'start_time', '<=', vals_list['visitor_booked'][0][2]['end_time']), '&', (
                 'end_time', '>=', vals_list['visitor_booked'][0][2]['start_time']), (
                 'end_time', '<=', vals_list['visitor_booked'][0][2]['end_time']),
             ('date', '=', vals_list['visitor_booked'][0][2]['date'])])
        print(booked_list)
        booked_eployees = set()
        for booked in booked_list:
            booked_eployees.add(booked.employees.id)

        print(booked_eployees)
        for rec in vals_list['visitor_booked'][0][2]['employees'][0][2]:
            if rec in booked_eployees:
                raise ValidationError("not work")

        print(set(vals_list['visitor_booked'][0][2]['employees'][0][2]))

        # employee_details = self.env['booked.schedule'].search([('visitor_name', 'not in', vals_list['visitor_booked'][0][2]['employees'][0][2])])

        records = super(VisitorCheckInOut, self).create(vals_list)
        return records

    def check_out(self):
        vals = {
            'check_out_time': datetime.datetime.now(),
            'check_in_status': False
        }
        self.write(vals)

    is_internal = fields.Boolean(string='Internal', )
    visitor_name = fields.Many2one('smart_visitor', string='Visitor Name', domain="[('is_internal','=',is_internal)]")
    email = fields.Char(related='visitor_name.email', string='Email')
    phone = fields.Char(related='visitor_name.phone_number', string='Phone')
    come_from = fields.Char(string='Come From')
    purpose = fields.Text(strig='Purpose')
    check_in_time = fields.Datetime(string="Check in Time")
    check_out_time = fields.Datetime(string="Check out Time")
    image = fields.Binary(string="Image", attachment=True)
    check_in_status = fields.Boolean(string='Check In Status', default=False)
    visitor_booked = fields.One2many('booked.schedule', 'visitor_id', string="Visitor")
