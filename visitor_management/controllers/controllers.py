# -*- coding: utf-8 -*-
# from odoo import http


# class VisitorManagement(http.Controller):
#     @http.route('/visitor_management/visitor_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visitor_management/visitor_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('visitor_management.listing', {
#             'root': '/visitor_management/visitor_management',
#             'objects': http.request.env['visitor_management.visitor_management'].search([]),
#         })

#     @http.route('/visitor_management/visitor_management/objects/<model("visitor_management.visitor_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visitor_management.object', {
#             'object': obj
#         })
