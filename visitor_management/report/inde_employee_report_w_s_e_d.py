from odoo import models, api


class genaeateEmployeeReport(models.AbstractModel):
    _name = 'report.visitor_management.indi_employee_report_w_s_e_d'
    _description = 'this is used for model extend patient_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(data)

        user_info = self.env['visitor_management.employee'].browse(data['employee_name'])
        user_checkin_out_info = self.env['visitor_management.employee.checkincheckout'].search(
            [('employee_name', '=', data['employee_name']), ('check_in_time', '>=', data['start_date']),
             ('check_in_time', '<=', data['end_date'])])
        print(user_checkin_out_info)

        return {

            'doc_model': 'visitor_management.employee',
            'docs': user_info,
            'check_model': 'visitor_management.employee.checkincheckout',
            'checks': user_checkin_out_info,

        }
