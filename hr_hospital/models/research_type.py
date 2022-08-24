from odoo import models, fields


class ResearchType(models.Model):
    _name = 'hr.hospital.research.type'
    _description = 'Research type'

    name = fields.Char()
    parent_id = fields.Many2one(comodel_name='hr.hospital.research.type', string='Parent Category', index=True, ondelete='cascade')
