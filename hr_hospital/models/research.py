from odoo import models, fields, api


class Research(models.Model):
    _name = 'hr.hospital.research'
    _description = 'Research'

    name = fields.Char()
    date_research = fields.Date()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Doctor')
    doctor_name = fields.Char()
    doctor_phone = fields.Char(string='phone')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient', string='patient')
    research_type_id = fields.Many2one(comodel_name='hr.hospital.research.type', string='research_type')
    sample_id = fields.Many2one(comodel_name='hr.hospital.sample', string='sample')
    sample_type_id = fields.Many2one(comodel_name='hr.hospital.sample.type', string='sample_type')

    conclusion = fields.Text()
    diagnosis_ids = fields.One2many(string="Diagnosis", comodel_name='hr.hospital.diagnosis', inverse_name='research_id', help="Diagnosis")
