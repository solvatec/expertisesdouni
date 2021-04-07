# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------
    reffered_id = fields.Many2one(
        comodel_name='res.partner',
        string='Apporté par'
    )

 

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------
