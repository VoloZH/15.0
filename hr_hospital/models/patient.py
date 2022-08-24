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
    doctor_id = fields.Many2one(string="Personal doctor",
                                comodel_name="hr.hospital.doctor",
                                ondelete="restrict")
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

    def hr_hospital_visit_to_doctor_act_window(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Visits",
            "res_model": "hr.hospital.visit.to.doctor",
            "view_type": "form",
            "view_mode": "tree,form",
            "domain": [("patient_id", "=", self.id)],
            "target": "current",
        }

    def open_list_history_of_personal_doctor(self):
        self.ensure_one()
        result = {
            "type": "ir.actions.act_window",
            "res_model": "hr.hospital.history.of.personal.doctor",
            "name": "personal doctor history",
            'view_mode': 'tree,form',
        }
        return result

    def open_list_diagnosis(self):
        self.ensure_one()
        result = {
            "type": "ir.actions.act_window",
            "res_model": "hr.hospital.diagnosis",
            "name": "diagnosis",
            'view_mode': 'tree,form',
        }
        return result

