# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date as fDate
import base64

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
    _rec_name = 'employee_id'

    """ employee_id = fields.Many2one('hr.employee', string = 'Empleado' ) """    
    employee_id = fields.Many2one('res.partner', string = 'Persona', domain=[('is_company','=',False)] )

    order_id = fields.Many2one('sale.order', string='Contrato')

    fecha_alta_contrato = fields.Date('Fecha alta contrato', default=fDate.today())

    task_type_id = fields.Many2one('hr.employee.task.type', string='Tipo de tarea')

    tipo_recurso = fields.Many2one('hr.employee.recurso.tipo', string='Tipo de recurso')

    requisitos_completos = fields.Boolean('Requisitos Completos', default=False)

    employee_ids = fields.One2many('sale.contract.employee.requirement', 'contract_employee_id', string='RRHH')

    @api.multi
    def action_requisitos(self):
        # import pdb; pdb.set_trace()     
              
        requisitos_ids = self.env['sale.contract.employee.requirement.recurso.tipo'].search([('tipo_recurso_id','=',self.tipo_recurso.id)])

        # import pdb; pdb.set_trace()

        for requisito in requisitos_ids:      
            cargado = self.env['sale.contract.employee.requirement'].search([('requisito_contrato_id','=',requisito.requisito_contrato_id.id), 
                                                                            ('contract_employee_id','=',self.id)])
            #import pdb; pdb.set_trace()
            if not(cargado):
                vals = {'contract_employee_id': self.id,'requisito_contrato_id': requisito.requisito_contrato_id.id}
                self.env['sale.contract.employee.requirement'].create(vals)

        return True

class ContractEmployeeRequirement(models.Model):
    """"""

    _name = 'sale.contract.employee.requirement'
    _description = 'Requisitos empleado'
    _inherit = ['mail.thread']

    contract_employee_id = fields.Many2one('sale.contract.employee', string='Correlativo RRHH')

    requisito_contrato_id = fields.Many2one('sale.contract.employee.requirement.type', string='Requisito contrato')

    requisito_cumplido = fields.Boolean('Requisito cumplido', default=False)

    imagen = fields.Binary('Imagen')

    doc_attachment_id = fields.Many2many('ir.attachment', 'sale_contract_employee_requirement_attach_rel', 
                                        'doc_id', 'attach_id3', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)


class RequirementAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel = fields.Many2many('sale.contract.employee.requirement', 'doc_attachment_id', 'attach_id3', 'doc_id',
                                      string="Attachment", invisible=1)


class ContractEmployeeRequirementRecursoTipo(models.Model):
    """"""

    _name = 'sale.contract.employee.requirement.recurso.tipo'
    _description = 'Requisitos RRHH segun tipo recurso'
    _inherit = ['mail.thread']

    tipo_recurso_id = fields.Many2one('hr.employee.recurso.tipo', 'Tipo Recurso')

    requisito_contrato_id = fields.Many2one('sale.contract.employee.requirement.type', string='Requisito contrato') 

class ContractEmployeeRequirementType(models.Model):
    _name = 'sale.contract.employee.requirement.type'
    _inherit = ['mail.thread']
    _description = 'Tipos de requerimientos'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')
    tiene_vencimiento = fields.Boolean('Tiene vencimiento?', default=False)
    habilitacion_asociada = fields.Many2one('hr.employee.habilitacion.tipo', string='Habilitacion Asociada')

class EmployeeTaskType(models.Model):
    _name = 'hr.employee.task.type'
    _inherit = ['mail.thread']
    _description = 'Tipos de tareas'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')

class EmployeeHabilitacionTipo(models.Model):
    _name = 'hr.employee.habilitacion.tipo'
    _inherit = ['mail.thread']
    _description = 'Tipos de habilitaciones'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')

class EmployeeRecursoTipo(models.Model):
    _name = 'hr.employee.recurso.tipo'
    _inherit = ['mail.thread']
    _description = 'Tipos de recursos'
    _rec_name = 'descripcion'

    descripcion = fields.Char('Descripción')
    observaciones = fields.Char('Observaciones')

class ContractVehicle(models.Model):
    """"""

    _name = 'sale.contract.vehicle'
    _description = 'Vehículos asignados'
    
    vehicle_id = fields.Many2one('fleet.vehicle', string = 'Vehículo' )    
    
    order_id = fields.Many2one('sale.order', string='Contrato')

class ResPartner(models.Model):
    _inherit = 'res.partner'
