# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------
    # ice = fields.Char(
    #     string='ICE',
    #     required=False,
    # )

    date_embauche = fields.Date(
        string='Date d’embauche',
    )

    cnss = fields.Char(
        string='N° CNSS',
    )

    cimr = fields.Char(
        string='N° CIMR',
    )

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------

    # @api.constrains('rc', 'cnss', 'ice', 'company_type')
    # def check_fields(self):
    #     for record in self:
    #         if self.company_type == 'company':
    #             related_ice = self.env['res.partner'].search([('id', '!=', self.id), ('ice', '=', self.ice)])
    #             related_rc = self.env['res.partner'].search([('id', '!=', self.id), ('rc', '=', self.rc)])
    #             related_cnss = self.env['res.partner'].search([('id', '!=', self.id),('cnss', '=', self.cnss)])
    #             if record.ice:
    #                 if len(record.ice) !=15 and len(record.ice) !=9:
    #                     raise ValidationError(_('ICE doit contenir 15 ou 9 caractères ! %s')  % (record.name))
    #             else:
    #                 raise ValidationError(_('Merci de renseigner ICE ! %s')  % (record.name))