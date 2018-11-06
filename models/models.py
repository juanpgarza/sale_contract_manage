# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date as fDate

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
    _inherit = ['mail.thread']
    _description = 'HHRR asignados'

    employee_id = fields.Many2one('hr.employee', string = 'Empleado' )    
    
    order_id = fields.Many2one('sale.order', string='Contrato')

    fecha_alta_contrato = fields.Date('Fecha alta contrato', default=fDate.today())

    requisitos_completos = fields.Boolean('Requisitos Completos', default=False)


class ContractEmployeeRequirement(models.Model):
    """"""

    _name = 'sale.contract.employee.requirement'
    _description = 'Requisitos empleado'

    requisito_cumplido = fields.Boolean('Requisito cumplido', default=False)

class ContractEmployeeRequirementType(models.Model):
    _name = 'sale.contract.employee.requirement.type'
    _description = 'Tipos de requerimientos'

    descripcion = fields.Char('Descripción')

class EmployeeTaskType(models.Model):
    _name = 'hr.employee.task.type'
    _descripcion = 'Tipos de tareas'

    descripcion = fields.Char('Descripción')

class ContractVehicle(models.Model):
    """"""

    _name = 'sale.contract.vehicle'
    _description = 'Vehículos asignados'

    vehicle_id = fields.Many2one('fleet.vehicle', string = 'Vehículo' )    
    
    order_id = fields.Many2one('sale.order', string='Contrato')