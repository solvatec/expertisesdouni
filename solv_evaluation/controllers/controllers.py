# -*- coding: utf-8 -*-
from odoo import http

# class SolvModule(http.Controller):
#     @http.route('/solv_module/solv_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/solv_module/solv_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('solv_module.listing', {
#             'root': '/solv_module/solv_module',
#             'objects': http.request.env['solv_module.solv_module'].search([]),
#         })

#     @http.route('/solv_module/solv_module/objects/<model("solv_module.solv_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('solv_module.object', {
#             'object': obj
#         })