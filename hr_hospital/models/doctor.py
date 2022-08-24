import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hr.hospital.person.mixin'

    specialty = fields.Char()
    intern = fields.Boolean(string="Intern",
                            default=False)
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Mentor for intern', domain="[('intern', '=', False)]")
    intern_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='mentor_id', string='interns')
    mentor_ids = fields.One2many(comodel_name='hr.hospital.doctor', inverse_name='mentor_id', string='mentors')
    personal_patient_ids = fields.One2many(comodel_name='hr.hospital.patient', inverse_name='personal_doctor_id', string='personal patients')
    patient_ids = fields.One2many(string="personal patients",
                                  comodel_name="hr.hospital.patient",
                                  inverse_name="doctor_id")

    def hr_hospital_add_visit_from_doctor_view(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Visit",
            "res_model": "hr.hospital.visit.to.doctor",
            "view_type": "form",
            "view_mode": "form",
            #  "context": {"default_patient_id": self.ids[0]},
            'view_id': self.env.ref("hr_hospital.hr_hospital_visit_to_doctor_form").id,
            "target": "new",
        }
