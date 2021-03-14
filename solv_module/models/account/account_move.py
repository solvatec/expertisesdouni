# -*- encoding: utf-8 -*-
##############################################################################

from odoo import fields, api, models, _



class AccountMove(models.Model):

    _inherit = "account.move"


##############################################################################
# FIELDS
##############################################################################

    # payment_type_invoice = fields.Selection(
    #     string= 'Type de paiement',
    #     selection= 'get_payment_type',
    #     required= False
    # )

##############################################################################
# METHODS
##############################################################################
    # def get_payment_type(self):
    #     return [
    #         ('espece',_('Espèce')),
    #         ('cheque',_('Chèque')),
    #         ('effet',_('Effet')),
    #         ('virement',_('Virement')),
    #     ]

