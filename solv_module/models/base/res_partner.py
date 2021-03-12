# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------
    # ice = fields.Char(
    #     string='ICE',
    #     required=False,
    # )

    fax = fields.Char(
        string='FAX',
    )

    rc = fields.Char(
        string='RC',
    )

    cnss = fields.Char(
        string='CNSS',
    )

    if_partner = fields.Char(
        string='IF',
    )

    patente = fields.Char(
        string='Patente',
    )

    capital = fields.Float(
        string='Capital',
    )


    nbr_employee = fields.Integer(
    	string='Nbre employes',
    )

    # ------------------------------------------------------------------------
    # CONSTRAINTS
    # ------------------------------------------------------------------------

    _sql_constraints = [
        ('ice', 'CHECK(1=1)', 'Le champ ICE est deja existant !'),
        ('rc', 'CHECK(1=1)', 'Le champ RC est deja existant !'),
        ('cnss', 'CHECK(1=1)', 'Le champ CNSS est deja existant !'),
        ('if_partner', 'CHECK(1=1)', 'Le champ IF est deja existant !'),
        # ('ice', 'UNIQUE (ice)', 'Le champ ICE est unique !'),
    ]

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
