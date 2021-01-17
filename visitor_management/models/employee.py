from odoo import models, fields, api, _


class EmployeeProfile(models.Model):
    _name = 'visitor_management.employee'
    _description = 'this model is store all data of employee info '
    _rec_name = 'e_id'
    designation = [('manager', 'Manger'),
                   ('project_manager', 'Project Manager'),
                   ('sr_software_developer', 'Sr. Software Developer'),
                   ('software_developer', 'Software Developer'),
                   ('jr_software_developer', 'Jr. Software Developer'),
                   ('software_developer_trainee', 'Software Developer Trainee'),
                   ('others', 'Others')]
    dept = [('software', 'Software'),
            ('it', 'It'),
            ('others', 'Others')]

    def name_get(self):
        # name get function for the model executes automatically
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.e_id, rec.e_name)))
        return res

    e_id = fields.Char(string='Employee Id', required=True, size=14)
    e_name = fields.Char(string='Employee Name', required=True)
    e_phone_number = fields.Char(string='Employee Phone_number', required=True, size=14)
    e_email = fields.Char(string='Email')
    e_designation = fields.Selection(designation, required=True, default='software_developer_trainee',
                                     string='Designation')
    department = fields.Selection(dept, required=True, default='software',
                                  string='Department')
    e_image = fields.Binary(string="Image", attachment=True)
    employee_ref_user = fields.Many2one('res.users', string="Login id")
