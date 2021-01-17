from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import datetime


class EmployeeCheckinCheckoutTime(models.Model):
    _name = 'visitor_management.employee.checkincheckout'
    _description = 'this is store all visitor check in and check out time '
    _rec_name = 'employee_name'
    check_out_stat = [
        ('auto', 'Auto'),
        ('manual', 'Manual')
    ]

    @api.model
    def create(self, vals_list):

        print(vals_list)

        if 'check_out_time' not in vals_list.keys():
            vals_list['check_in_time'] = datetime.datetime.now()
            objects = self.search([('status', '=', False)])
            for single in objects:
                # print('val : '+str(vals_list.get('employee_name'))+" == single: "+str(single.employee_name.id))
                if vals_list.get('employee_name') == single.employee_name.id:
                    raise ValidationError(_('You can not create new visit until  checked out !'))

            result = super(EmployeeCheckinCheckoutTime, self).create(vals_list)
            print(result)
            return result
        else:
            employee_id = vals_list.get('employee_name')
            objects = self.search([('employee_name', '=', employee_id), ('status', '=', False)])
            if len(objects) > 0:
                print(" update result : ", objects)
                vals_list['status'] = True
                vals_list['check_out_status'] = 'manual'
                vals_list['check_out_time'] = datetime.datetime.now()
                print(vals_list)
                objects.write(vals_list)
                print(objects)
                return objects
            else:
                raise ValidationError("please check in first")

    employee_name = fields.Many2one('visitor_management.employee', string='Employee', required=True)
    check_in_time = fields.Datetime(string="Check in Time")
    check_out_time = fields.Datetime(string="Check out Time")
    status = fields.Boolean(string='Is checkout ', default=False)
    check_out_status = fields.Selection(check_out_stat)
