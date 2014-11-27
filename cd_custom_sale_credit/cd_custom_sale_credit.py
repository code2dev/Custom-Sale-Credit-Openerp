 # -*- coding: utf-8 -*-
##############################################################################
#    
# Module : cd_custom_sale
# Author : 2014-03-28 G Lopez @glopzvega
#
# Modulo que permite mostrar la informacion de credito desde la cotizacion
#
##############################################################################

import openerp
from openerp.osv import osv, fields

class sale_order_custom(osv.osv) :     
    _inherit = "sale.order"    

    _columns = {
#     	"property_payment_term" : fields.char('Condiciones de Pago'),    	
    	"credit_limit" : fields.float('Limite de Credito', store=True),    	
    	"credit" : fields.float('Credito', store=True),  
        "date_entrega" : fields.date("Fecha Entrega")  	
    }
    
    def create(self, cr, uid, vals, context=None):    
        
        if vals.get("partner_id") : 
            partner = self.pool.get('res.partner').browse(cr, uid, vals["partner_id"], context=context)
            vals["credit"] = float(partner.credit)
            vals["credit_limit"] = partner.credit_limit    
            vals["payment_term"] = partner.property_payment_term and partner.property_payment_term.id or False
        
        return super(sale_order_custom, self).create(cr, uid, vals, context=context)
    
    def write(self, cr, uid, ids, vals, context=None):
        
        if vals.get("partner_id") :        
            partner = self.pool.get('res.partner').browse(cr, uid, vals["partner_id"], context=context)
            vals["credit"] = float(partner.credit)
            vals["credit_limit"] = partner.credit_limit    
            vals["payment_term"] = partner.property_payment_term and partner.property_payment_term.id or False    
        
        return super(sale_order_custom, self).write(cr, uid, ids, vals, context=context)

    def onchange_partner_id(self, cr, uid, ids, part, context=None):    	

        result = super(sale_order_custom, self).onchange_partner_id(cr, uid, ids, part, context=context)
        result = result["value"] 
        
        partner = self.pool.get('res.partner').browse(cr, uid, part, context=context)
        
#         values = {
#              "credit" : part.credit,
#              "credit_limit" : part.credit_limit,
#              "property_payment_term" : part.property_payment_term.name
#     	}payment_term = part.property_payment_term and part.property_payment_term.id or False
        result.update({
                       "credit" : partner.credit, 
                       "credit_limit" : partner.credit_limit, 
#                        "property_payment_term" : partner.property_payment_term and partner.property_payment_term.name or False
        })
        return {'value' : result}

sale_order_custom()