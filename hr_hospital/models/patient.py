import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    first_name = fields.Char()
    second_name = fields.Char()

    active = fields.Boolean(
        default=True, )
