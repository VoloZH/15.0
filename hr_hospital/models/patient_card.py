import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientCard(models.Model):
    _name = 'hr.hospital.patient.card'
    _description = 'Patient Card'

    patient_card_ids = fields.Integer()
    date = fields.Date()

    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor', )
