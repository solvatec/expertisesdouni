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

    partner_type_id = fields.Many2one(
        comodel_name='partner.type',
        string='Type de compte'
    )

    # Sites
    partner_site_ids = fields.Many2many(
        string='Sites',
        comodel_name='res.partner',
        relation='site_res_partner_rel',
        column1='parent_id',
        column2='site_partner_id',
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

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        # return values in result, as this method is used by _fields_sync()
        if not self.parent_id:
            return
        result = {}
        partner = self._origin
        if partner.parent_id and partner.parent_id != self.parent_id:
            result['warning'] = {
                'title': _('Warning'),
                'message': _('Changing the company of a contact should only be done if it '
                             'was never correctly set. If an existing contact starts working for a new '
                             'company then a new contact should be created under that new '
                             'company. You can use the "Discard" button to abandon this change.')}
        return result

class PartnerType(models.Model):
    _name = 'partner.type'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )