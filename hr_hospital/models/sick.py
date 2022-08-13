from odoo import models, fields


class Sick(models.Model):
    _name = 'hr.hospital.sick'
    _description = 'Sick'

    name = fields.Char()

    sick_type_id = fields.Many2one(comodel_name='hr.hospital.sick.type', string='sick type', index=True, ondelete='cascade')
    parent_id = fields.Many2one(comodel_name='hr.hospital.sick', string='Parent Category', index=True, ondelete='cascade')
