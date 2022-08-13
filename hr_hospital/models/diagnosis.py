import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    sick_id = fields.Many2one(comodel_name='hr.hospital.sick')
    sick_type = fields.Char()
    prescribed_treatment = fields.Char()
    date_of_diagnosis = fields.Date()
    research_id = fields.Many2one('hr.hospital.research')
