import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HistoryOfPersonalDoctor(models.Model):
    _name = 'hr.hospital.history.of.personal.doctor'
    _description = 'History of personal Doctor'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient', string='Patient')
    sick_id = fields.Many2one(comodel_name='hr.hospital.sick', string='sick')
    date_diagnosis = fields.Date()
