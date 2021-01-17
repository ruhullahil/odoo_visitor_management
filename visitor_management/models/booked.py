from odoo import models, fields, api, _


class BookedSchedule(models.Model):
    _name = 'visitor_management.booked_schedule'
    _description = 'this use for storing book info'

    # domain=lambda self: self.show_slot
    # domain=lambda self: [('id', 'not in', self.env['visitor_management.datetime.slot'].search([]).id)]
    #
    slot = fields.Many2one('visitor_management.datetime.slot', string='Slot', domain=lambda self: self.show_slot())
    visitor = fields.Many2one('visitor_management.visitor', string='Visitor name')

    def show_slot(self):
        booked_list = self.env['visitor_management.booked_schedule'].search([])
        print(booked_list)
        booked_id_list = []
        for rec in booked_list:
            booked_id_list.append(rec.slot.id)
        print('booked id list : ', booked_id_list)
        # name_slot = self.env['visitor_management.datetime.slot'].search([('id', 'not in', booked_id_list)])
        # book_t=tuple(booked_id_list)
        print('name slot : ', [('id', 'not in ', booked_id_list)])
        # return[name_slot]

        return [('id', 'not in', booked_id_list)]
