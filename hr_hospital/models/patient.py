import datetime
import logging

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = 'hr.hospital.person.mixin'

    birthday = fields.Date()
    age = fields.Char(compute='_compute_age')
    passport = fields.Char()
    contact_person_id = fields.Many2one(comodel_name='hr.hospital.contact.person')
    personal_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    history_of_personal_doctor_ids = fields.One2many(comodel_name='hr.hospital.history.of.personal.doctor', inverse_name='patient_id')
    visit_to_doctor_ids = fields.One2many(comodel_name='hr.hospital.visit.to.doctor', inverse_name='patient_id', string='visits history')
 #   patient_id = fields.Many2one(comodel_name='hr.hospital.doctor.multi.wizard')

    @api.depends('birthday')
    def _compute_age(self):
        today_date = datetime.date.today()
        for rec in self:
            if rec.birthday:
                birthday = fields.Datetime.to_datetime(rec.birthday).date()
                difference_in_years = relativedelta(today_date, birthday).years
                rec.age = difference_in_years
            else:
                rec.age = "Not Provided...."