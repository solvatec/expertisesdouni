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
        string='Nombre d’employés',
    )

    # Sites
    partner_site_ids = fields.Many2many(
        string='Sites',
        comodel_name='res.partner',
        relation='site_res_partner_rel',
        column1='parent_id',
        column2='site_partner_id',
    )

    partner_type_id = fields.Many2one(
        comodel_name='partner.type',
        string='Type de compte'
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

    @api.model
    def get_selection_partner_type(self):
        return [
            ('prospect', _('Prospect')),
            ('assureur', _('Assureur')),
            ('assureur_conseil', _('Assureur Conseil')),
            ('expert_cie', _('Expert Cie')),
        ]

class PartnerType(models.Model):
    _name = 'partner.type'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )