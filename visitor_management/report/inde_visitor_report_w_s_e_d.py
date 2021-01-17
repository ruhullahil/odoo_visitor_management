from odoo import models, api


class genaeateVisitorReport(models.AbstractModel):
    _name = 'report.visitor_management.indi_visitor_report_w_s_e_d'
    _description = 'this is used for model visitor'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(data)

        user_info = self.env['visitor_management.visitor'].browse(data['visitor_name'])
        user_checkin_out_info = self.env['visitor_management.visitor.checkincheckout'].search(
            [('visitor_name', '=', data['visitor_name']), ('check_in_time', '>=', data['start_date']),
             ('check_in_time', '<=', data['end_date'])])
        print(user_checkin_out_info)

        return {

            'doc_model': 'visitor_management.visitor',
            'docs': user_info,
            'check_model': 'visitor_management.visitor.checkincheckout',
            'checks': user_checkin_out_info,

        }
