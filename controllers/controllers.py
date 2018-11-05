# -*- coding: utf-8 -*-
from odoo import http

# class SaleContractManage(http.Controller):
#     @http.route('/sale_contract_manage/sale_contract_manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_contract_manage/sale_contract_manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_contract_manage.listing', {
#             'root': '/sale_contract_manage/sale_contract_manage',
#             'objects': http.request.env['sale_contract_manage.sale_contract_manage'].search([]),
#         })

#     @http.route('/sale_contract_manage/sale_contract_manage/objects/<model("sale_contract_manage.sale_contract_manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_contract_manage.object', {
#             'object': obj
#         })