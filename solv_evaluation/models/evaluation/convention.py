# -*- coding: utf-8 -*-
from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError, Warning, UserError
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    collaborator_id = fields.Many2one(
        string="Type",
        comodel_name='type.collaborator',
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
    # METHODS
    # ------------------------------------------------------------------------