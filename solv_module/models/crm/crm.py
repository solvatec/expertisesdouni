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

    is_partner = fields.Boolean(
        string='Est un client',
        compute='get_is_partner'
    ) 

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------
    @api.model
    def get_is_partner(self):
        for record in self:
            if record.partner_id.customer_rank!=0:
                record.is_partner=True
            else:
                record.is_partner=False

