from odoo import models, fields, api, _


class DateTimeSlot(models.Model):
    _name = 'visitor_management.datetime.slot'
    _description = 'this is time slot table where we store all time and all employee schedule'

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id,
                        '%s - %s Time(%.2f:%.2f)' % (rec.date, rec.employee_slot.e_name, rec.start_time, rec.end_time)))
        return res

    date = fields.Date(string='Date')
    start_time = fields.Float(string='Start Time')
    end_time = fields.Float(string='End Time')
    employee_slot = fields.Many2many('visitor_management.employee', 'time_slot_employee_rel',
                                     string='Employee available')
