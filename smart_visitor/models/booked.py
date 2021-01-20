from odoo import models, fields, api


class BookedSchedule(models.Model):
    _name = 'booked.schedule'

    def cal_duration(self):
        for rec in self:
            return rec.end_time - rec.start_time

    employees = fields.Many2many('smart_visitor', 'employee_rel_booked', string='Employees')
    visitors = fields.Many2many('smart_visitor', 'visitor_rel_booked', string='Visitors')
    date = fields.Date(string='Date')
    start_time = fields.Float(string='Start Time')
    end_time = fields.Float(string='End Time')
    duration = fields.Float(string='Duration', compute='cal_duration')
    meeting_note = fields.Text(string='Note')
    visitor_id = fields.Many2one('visitor.check.in.out', string="Visitor Check In")


