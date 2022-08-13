from odoo import models, fields


class Sample(models.Model):
    _name = 'hr.hospital.sample'
    _description = 'Sample'

    name = fields.Char()

    sample_type_id = fields.Many2one(comodel_name='hr.hospital.sample.type', string='sample_type')
