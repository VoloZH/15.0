import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hr.hospital.person.mixin'

    specialty = fields.Char()
    intern = fields.Boolean()
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Mentor for intern', domain="[('intern', '=', False)]")
    intern_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='mentor_id', string='interns')
    mentor_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='mentor_id', string='mentors')
    personal_patient_ids = fields.One2many(comodel_name='hr.hospital.patient', inverse_name='personal_doctor_id', string='personal patients')


