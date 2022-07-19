import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    first_name = fields.Char()
    second_name = fields.Char()
