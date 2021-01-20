# -*- coding: utf-8 -*-
# from odoo import http


# class SmartVisitor(http.Controller):
#     @http.route('/smart_visitor/smart_visitor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smart_visitor/smart_visitor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_visitor.listing', {
#             'root': '/smart_visitor/smart_visitor',
#             'objects': http.request.env['smart_visitor.smart_visitor'].search([]),
#         })

#     @http.route('/smart_visitor/smart_visitor/objects/<model("smart_visitor.smart_visitor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_visitor.object', {
#             'object': obj
#         })
