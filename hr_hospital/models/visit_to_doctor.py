import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class VisitToDoctor(models.Model):
    _name = 'hr.hospital.visit.to.doctor'
    _description = 'Visit to Doctor'

    name = fields.Char()
    date_of_visit = fields.Date()
    time_of_visit = fields.Datetime()
    state = fields.Integer()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient', string='Patient')
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis', string='Diagnosis')
    recommendation = fields.Char()


