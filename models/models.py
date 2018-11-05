# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    employee_ids = fields.One2many('sale.contract.employee', 
                                'order_id', 
                                string= 'Empleados asignados al contrato' )

    vehicle_ids = fields.One2many('sale.contract.vehicle', 
                                'order_id', 
                                string= 'Vehículos asignados al contrato' )

    fecha_contrato = fields.Date('Fecha Contrato')

    active = fields.Boolean('Activo')

class ContractEmployee(models.Model):
    """"""

    _name = 'sale.contract.employee'
    _description = 'HHRR asignados'

    employee_id = fields.Many2one('hr.employee', string = 'Empleado' )    
    
    order_id = fields.Many2one('sale.order', string='Contrato')

class ContractVehicle(models.Model):
    """"""

    _name = 'sale.contract.vehicle'
    _description = 'Vehículos asignados'

    vehicle_id = fields.Many2one('fleet.vehicle', string = 'Vehículo' )    
    
    order_id = fields.Many2one('sale.order', string='Contrato')