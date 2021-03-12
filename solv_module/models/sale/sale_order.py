# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools import float_compare

import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

# class SaleOrderLine(models.Model):
#     _inherit = "sale.order.line"

#     @api.onchange('product_id')
#     def product_id_change(self):
#         res = super(SaleOrderLine, self).product_id_change()
#         if  self.product_id:
#             product = self.product_id
#             self.name = product.name
#         return res