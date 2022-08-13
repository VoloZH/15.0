import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PersonMixin(models.AbstractModel):
    _name = 'hr.hospital.person.mixin'
    _description = 'Person mixin'

    first_name = fields.Char()
    second_name = fields.Char()
    gender = fields.Selection(default='other', selection=[('male','Male'), ('female','Female'),('other','Other/Undefined')],)
    email = fields.Char()
    phone_number = fields.Integer()
    photo = fields.Binary()
