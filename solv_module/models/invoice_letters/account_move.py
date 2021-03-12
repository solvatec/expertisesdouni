# -*- encoding: utf-8 -*-
##############################################################################

from odoo import fields, api, models, _



class AccountMove(models.Model):

    _inherit = "account.move"
    

##############################################################################
# METHODS
##############################################################################


    @api.depends('amount_total')
    def get_amount_letter(self):
        amount = self.currency_id.amount_to_text(self.amount_total)
        return amount

class SaleOrder(models.Model):

    _inherit = "sale.order"
	
    @api.depends('amount_total')
    def get_amount_letter(self):
        amount = self.currency_id.amount_to_text(self.amount_total)
        return amount

