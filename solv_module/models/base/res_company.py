# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = 'res.company'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------
    ice = fields.Char(
        string='ICE',
        required=False,
    )

    rc = fields.Char(
        string='RC',
    )

    cnss = fields.Char(
        string='CNSS',
    )

    if_company = fields.Char(
        string='IF',
    )

    patente = fields.Char(
        string='Patente',
    )

    capital = fields.Float(
        string='Capital',
    )

    fax = fields.Char(
        string='FAX',
        required=False,
    )

    # ------------------------------------------------------------------------
    # CONSTRAINTS
    # ------------------------------------------------------------------------

    _sql_constraints = [
        ('ice', 'CHECK(1=1)', 'Le champ ICE est deja existant !'),
        ('rc', 'CHECK(1=1)', 'Le champ RC est deja existant !'),
        ('cnss', 'CHECK(1=1)', 'Le champ CNSS est deja existant !'),
        ('if_company', 'CHECK(1=1)', 'Le champ IF est deja existant !'),
        ('ice', 'UNIQUE (ice)', 'Le champ ICE est unique !'),
    ]