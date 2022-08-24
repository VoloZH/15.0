import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact person'
    _inherit = ['hr.hospital.person.mixin', ]
