from odoo import models, api


class genaeateEmployeeReport(models.AbstractModel):
    _name = 'report.visitor_management.all_visitor_report_w_s_e_d'
    _description = 'this is used for model visitor'

    @api.model
    def _get_report_values(self, docids, data=None):
        user_checkin_out_info = self.env['visitor_management.visitor.checkincheckout'].search(
            [('check_in_time', '>=', data['start_date']),
             ('check_in_time', '<=', data['end_date'])])

        employee_name = {'emp': set()}

        for employee in user_checkin_out_info:
            employee_name['emp'].add(employee.visitor_name)

        return {

            'check_model': 'visitor_management.visitor.checkincheckout',
            'checks': user_checkin_out_info,
            'tst': employee_name

        }
