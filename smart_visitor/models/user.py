from odoo import models, fields, api


class SmartVisitor(models.Model):
    _name = 'smart_visitor'
    _rec_name = 'user_name'
    _sql_constraints = [
        ('phone_number_unique', 'unique(phone_number)', 'Can\'t be duplicate value for this field!')
    ]

    designation = [('manager', 'Manger'),
                   ('project_manager', 'Project Manager'),
                   ('sr_software_developer', 'Sr. Software Developer'),
                   ('software_developer', 'Software Developer'),
                   ('jr_software_developer', 'Jr. Software Developer'),
                   ('software_developer_trainee', 'Software Developer Trainee'),
                   ('others', 'Others')]
    dept = [('software', 'Software'),
            ('it', 'IT'),
            ('others', 'Others')]

    is_internal = fields.Boolean(string='Internal', default=False, required=True)
    user_name = fields.Char(string='User Name', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    dept = fields.Selection(dept, string='Department')
    deg = fields.Selection(designation, string='Designation')
    emp_id = fields.Char(string='Employee id')
    image = fields.Binary(string="Image", attachment=True)
