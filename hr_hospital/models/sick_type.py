from odoo import models, fields


class SickType(models.Model):
    _name = 'hr.hospital.sick.type'
    _description = 'Sample type'

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name='hr.hospital.sick.type', string='Parent Category', index=True, ondelete='cascade')
