from odoo import models, fields, _
import datetime


class VisitorReport(models.TransientModel):
    _name = 'visitor_management.visitor.report'

    # object report generation
    def visitor_management_visitor_report(self):
        print('that\'s worked')

        if self.visitor_name.id:
            if not self.start_date:
                self.start_date = datetime.datetime(1990, 1, 1)
            if not self.end_date:
                self.end_date = datetime.datetime.now()
            data = {
                'visitor_name': self.visitor_name.id,
                'start_date': self.start_date,
                'end_date': self.end_date
            }
            return self.env.ref('visitor_management.individual_visitor_report_s2e_date').with_context(
                landscape=False).report_action(self, data=data)
        else:
            if not self.start_date:
                self.start_date = datetime.datetime(1990, 1, 1)
            if not self.end_date:
                self.end_date = datetime.datetime.now()
            data = {
                'start_date': self.start_date,
                'end_date': self.end_date
            }
            return self.env.ref('visitor_management.all_visitor_report_s2e_date').with_context(
                landscape=False).report_action(self, data=data)

    visitor_name = fields.Many2one('visitor_management.visitor', string='Visitor Name ')
    start_date = fields.Datetime(string='From (date)')
    end_date = fields.Datetime(string='To (date)')
