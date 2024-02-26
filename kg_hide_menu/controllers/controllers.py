# -*- coding: utf-8 -*-
# from odoo import http


# class KgHideMenu(http.Controller):
#     @http.route('/kg_hide_menu/kg_hide_menu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kg_hide_menu/kg_hide_menu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kg_hide_menu.listing', {
#             'root': '/kg_hide_menu/kg_hide_menu',
#             'objects': http.request.env['kg_hide_menu.kg_hide_menu'].search([]),
#         })

#     @http.route('/kg_hide_menu/kg_hide_menu/objects/<model("kg_hide_menu.kg_hide_menu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kg_hide_menu.object', {
#             'object': obj
#         })

