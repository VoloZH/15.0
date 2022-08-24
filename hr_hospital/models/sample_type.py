from odoo import models, fields


class SampleType(models.Model):
    _name = 'hr.hospital.sample.type'
    _description = 'Sample type'

    name = fields.Char()

