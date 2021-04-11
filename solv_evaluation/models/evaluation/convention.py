# -*- coding: utf-8 -*-
from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError, Warning, UserError
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

import logging

_logger = logging.getLogger(__name__)

class ProjectProject(models.Model):
    _inherit = 'project.project'
    # _inherit = 'mail.activity', 'mail.thread.cc', 'mail.activity.mixin', 'rating.mixin'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------
    activity_ids = fields.One2many(
        'mail.activity', 'res_id', 'Activities',
        auto_join=True,
        groups="base.group_user",)

    type_project = fields.Selection(
        string="Type projet",
        selection='get_selection_type_project',
        default='project',
    )

    # , group_expand='_expand_states'
    stage_id = fields.Many2one(
        comodel_name='project.stage', string='Stage', index=True, tracking=True,
        readonly=False, store=True, group_expand='_read_group_stage_ids', copy=False, ondelete='restrict',
        domain="['|', ('user_id', '=', False), ('user_id', '=', user_id)]"
    )


    num_dossier  = fields.Char(
        string="N° Dossier",
    )

    # partner_id = fields.Many2one(
    #     comodel_name='res.partner', 
    #     string='Groupe/ Société Mére',
    #     domain="[('is_company', '=', True)]"
    # )

    urgent  = fields.Boolean(
        string="Urgent",
    )

    partner_site_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Site',
        domain="[('is_company', '=', True)]"
    )

    partner_interm_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Intermediaire',
    )

    nature_mission = fields.Many2one(
        comodel_name='nature.mission', 
        string='Nature de la mission ',
    )

    nature_dossier  = fields.Selection(
        string="Nature Dossier",
        selection='get_selection_nature_dossier',
        default='dossier_initial',
    )

    type_maj  = fields.Selection(
        string="Type de Mise à jour",
        selection='get_selection_type_maj',
        default='annuel',
    )

    num_maj  = fields.Selection(
        string="N° MAJ",
        selection='get_selection_num_maj',
    )

    state_order  = fields.Selection(
        string="Etat commande",
        selection='get_selection_state_order',
    )

    scan_3d  = fields.Boolean(
        string="Scan 3D",
    )

    state  = fields.Selection(
        string="Etat",
        selection='get_selection_state',
    )

    # Collaborateurs
    # partner_ids = fields.Many2many(
    #     string='Collaborateurs',
    #     comodel_name='res.partner',
    #     relation='project_project_eval_partner_rel',
    #     column1='parent_id',
    #     column2='eval_partner_id',
    # )

    collaborator_ids = fields.One2many(
        string='Collaborateurs',
        comodel_name='collaborator.line',
        inverse_name='project_eval_id'
    )

    # Expert(s)
    expert_id = fields.Many2one(
        string='Expert',
        comodel_name='res.partner',
        # relation='project_project_expert_eval_partner_rel',
        # column1='parent_id',
        # column2='expert_eval_partner_id',
    )

    # Vérificateurs
    auditor_id = fields.Many2one(
        string='Vérificateur',
        comodel_name='res.partner',
        # relation='project_project_auditor_eval_partner_rel',
        # column1='parent_id',
        # column2='auditor_eval_partner_id',
    )

    # Assistant(e)
    assistant_id = fields.Many2one(
        string='Assistant(e)',
        comodel_name='res.partner',
        # relation='project_project_assistant_eval_partner_rel',
        # column1='parent_id',
        # column2='assistant_eval_partner_id',
    )

    # Dates de la Commande
    date = fields.Date(
        string='Crée le',
    )

    date_order = fields.Date(
        string='Date de commande',
    )

    date_due = fields.Date(
        string='Date d’échéance',
    )

    date_order_end = fields.Date(
        string='Commande Terminée le',
    )

    date_order_cancel = fields.Date(
        string='Date d’annulation',
    )

    # Autres dates
    date_expert_assign = fields.Date(
        string='Expert Assigné le',
    )

    date_intervention = fields.Date(
        string='Dates de Visite / Intervention',
    )

    date_visite_end = fields.Date(
        string='Visite Terminé le',
    )

    date_rprt_start = fields.Date(
        string='DEBUT RPRT/CHIFF LE',
    )

    date_rprt_end = fields.Date(
        string='RPRT/CHIFF terminé le',
    )

    date_remise_saisie = fields.Date(
        string='DATE REMISE A LA SAISIE',
    )

    date_saisie_start = fields.Date(
        string='DATE DÉBUT DE LA SAISIE',
    )

    date_saisie_end = fields.Date(
        string='SAISIE terminé le',
    )

    date_rprt_validate = fields.Date(
        string='RPRT/CHIFF remis à la validation le',
    )

    date_rprt_validated = fields.Date(
        string='Rapport Validé le',
    )

    date_montage = fields.Date(
        string='DATE DE MONTAGE',
    )

    date_remise_invoice = fields.Date(
        string='DATE REMISE A LA FACTURATION',
    )

    date_invoice_send = fields.Date(
        string='DATE ENVOI AU CLIENT ',
    )
    # Contacts de la commande
    partner_order_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Commandé par',
    )

    partner_principal_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Contact principale',
    )

    partner_on_site_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Contact sur site',
    )

    partner_report_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Rapport adressé à',
    )
    # Fichiers

    evaluation_report_doc_ids = fields.Many2many(
        comodel_name='ir.attachment', 
        relation='project_project_attachment_report_rel',
        column1='parent_id',
        column2='attachment_report_id',
        string='RAPPORT FINAL',
    )

    evaluation_doc_ids = fields.Many2many(
        comodel_name='ir.attachment', 
        relation='project_project_attachment_doc_rel',
        column1='parent_id',
        column2='attachment_doc_id',
        string='DOCUMENTS',
    )
    # SCAN 3D

    scan_3d_embed_doc_ids = fields.Many2many(
        comodel_name='ir.attachment', 
        relation='project_project_attachment_scan_3d_embed_rel',
        column1='parent_id',
        column2='attachment_scan_3d_embed_id',
        string='scan 3d embed',
    )
    # Facturation et Frais

    is_invoice = fields.Boolean(
        string='à Facturer',
    )

    invoice_state = fields.Selection(
        string="Facturation",
        selection='get_selection_invoice_state',
    )

    amount_invoice = fields.Float(
        string="Montant Facture",
    )

    commission_expert = fields.Float(
        string="Commission Expert",
    )

    commission_assistate = fields.Float(
        string="Commission Assistate(s)",
    )

    commission_partner = fields.Float(
        string="Commission Partenaire(s)",
    )

    amount_frais = fields.Float(
        string="Montant Frais",
    )
    # Modification
    update = fields.Html(
        string="Modification",
    )

    update_state = fields.Selection(
        string="Etat",
        selection='get_selection_update_state',
    )

    date_update = fields.Datetime(
        string="Modification demandé le",
    )

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------
    @api.model
    def get_selection_type_project(self):
        return [
            ('project', _('Projet')),
            ('evaluation', _('Evaluation')),
            ('sinistre', _('Sinistre'))
        ]

    def get_selection_nature_dossier(self):
        return [
            ('dossier_initial', _('DI-(dossier initial)')),
            ('mise_a_jour', _('MAJ-(mise à jour)')),
        ]

    def get_selection_type_maj(self):
        return [
            ('annuel', _('Annuel')),
            ('biennal', _('Biennal')),
        ]

    def get_selection_num_maj(self):
        return [
            ('1ere', _('1ère')),
            ('2eme', _('2ème')),
            ('3eme', _('3ème')),
            ('4eme', _('4ème')),
            ('5eme', _('5ème')),
        ]

    def get_selection_state_order(self):
        return [
            ('en_attente', _('En attente')),
            ('encours', _('En cours')),
            ('livree', _('Livrée')),
            ('terminee', _('Terminée')),
            ('Annulee', _('Annulée')),
        ]

    def get_selection_state(self):
        return [
            ('terminer', _('Marquer comme terminé')),
            ('modifier', _('Modification requise')),
        ]

    def get_selection_invoice_state(self):
        return [
            ('send', _('Facture envoyé')),
            ('paid', _('Payé')),
            ('partial', _('Partiellement payé')),
            ('not_paid', _('En retart')),
        ]

    def get_selection_update_state(self):
        return [
            ('encours', _('En cours')),
            ('updated', _('Modifié')),
            ('approuved', _('approuvé')),
        ]

    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['project.stage'].search([('type_project_stage','=','evaluation')])
        return stage_ids

    ### collaborateurs ###
    @api.onchange('expert_id','auditor_id','assistant_id','partner_ids.collaborator')
    def _get_collaborators(self):
        partners = self.env['res.partner'].search([('id', 'in', [self.expert_id.id,self.auditor_id.id,self.assistant_id.id])])
        for record in self:
            for line in partners:
                record.collaborator_ids.write({'partner_id': line.id})

class ProjectStage(models.Model):
    _name = 'project.stage'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )

    user_id = fields.Many2one(
        comodel_name='res.users', 
        string="Utilisateur", 
        default=lambda self: self.env.uid
    )

    description = fields.Text(
        string="Description",
    )

    type_project_stage = fields.Selection(
        string="Type projet",
        selection='get_selection_type_project_stage',
        default=False
    )

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------
    @api.model
    def get_selection_type_project_stage(self):
        return [
            ('project', _('Projet')),
            ('evaluation', _('Evaluation')),
            ('sinistre', _('Sinistre'))
        ]

class NatureMission(models.Model):
    _name = 'nature.mission'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    collaborator = fields.Char(
        string="Type",
    )

    # collaborator_id = fields.Many2one(
    #     string="Type",
    #     comodel_name='type.collaborator',
    # )

    # ------------------------------------------------------------------------
    # METHODS
    # ------------------------------------------------------------------------

class TypeCollaborator(models.Model):
    _name = 'type.collaborator'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    name = fields.Char(
        string='Nom',
    )

class CollaboratorLine(models.Model):
    _name = 'collaborator.line'

    # ------------------------------------------------------------------------
    # FIELDS
    # ------------------------------------------------------------------------

    project_eval_id = fields.Many2one(
        comodel_name='project.project',
        string='Evaluation',
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Collaborateur',
    )

    collaborator_type = fields.Char(
        string='Type',
    )
    
    