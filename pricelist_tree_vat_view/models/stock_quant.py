   ##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class StockQuant(models.Model):
    _inherit ='stock.quant'
    _name = 'stock.quant'

    listprice_price = fields.Float(
        related="product_id.product_tmpl_id.listprice_price",
        string="Precio de venta"
    )
    listprice_price2 = fields.Float(
        related="product_id.product_tmpl_id.listprice_price2",
        string="Precio de venta"
    )

