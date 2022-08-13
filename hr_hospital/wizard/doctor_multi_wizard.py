import logging

from odoo import _, models, fields

_logger = logging.getLogger(__name__)


class DoctorMultiWizard(models.TransientModel):
    _name = 'hr.hospital.doctor.multi.wizard'
    _description = 'Change Personal Doctor Multi Wizard'

    names = fields.Char('Patients Name')
    patient_ids = fields.Many2many(string='patients', comodel_name='hr.hospital.patient')
    personal_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Doctor')

    def set_doctor(self):
        for patient_id in self.patient_ids:
            patient_id.personal_doctor_id = self.personal_doctor_id
        return {}
    #     def action_open_wizard(self):
#         return {
#             'name': _('Create Personal doctor Wizard'),
#             'type': 'ir.actions.act.window',
#             'view_mode': 'form',
#             'res_model': 'hr.hospital.doctor.multi.wizard',
#             'target': 'new',
# #            'context': {'default_country_id': self.env.user.company_id.id}, ## mozhno peredaty za zamovchuvannym znachennya dlya polya country_id
#         }
#
#     def action_create_record(self):
#         patient_list = []
#         for vals in self.patient_ids:
#             patient_list.append(vals.id)
#         for vals in patient_list:
# #            rec = {
# #                'personal_doctor_id': self.doctor_id.id
# #            }
#             vals.doctor_id = self.doctor_id.id


#    def action_create_record(self):
#        print("Test print")
#        patient_list = []
#        for vals in self.patient_ids:
#            patient_list.append(vals.id)
#            print(patient_list)
#
#       vals = {
#            'personal_doctor_id': self.doctor_id.id
#        }
#        for vals in patient_list:
#            if vals =
#        print(vals)
#        self.env['hr.hospital.patient'].write(vals)

#        active_id = self._context.get('active_id')
#        self.env['hr.hospital.doctor.multi.wizard'].browse(active_id)
