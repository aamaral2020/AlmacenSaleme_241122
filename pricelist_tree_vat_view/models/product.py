   ##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit ='product.template'
    _name = 'product.template'

    listprice_price = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta"
    )
    listprice_price2 = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2"
    )
    listprice_price_vat = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta c/iva"
    )
    listprice_price2_vat = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2 c/iva"
    )

    def _compute_price(self):
        listprice_tree_view = self.env.user.company_id.tree_view_pricelist_id.id
        listprice_tree_view2 = self.env.user.company_id.tree_view_pricelist2_id.id
        for rec in self:
            if rec:
                price = rec.with_context(pricelist=listprice_tree_view).price
                rec.listprice_price = price
                res = rec.taxes_id.compute_all(price, product=rec, partner=self.env['res.partner'])
                rec.listprice_price_vat = res['total_included']

                try:
                    prod = self.env['product.product'].search([('product_tmpl_id','=',rec.id)])
                    price2 = prod.with_context(pricelist=listprice_tree_view2).price
                    res = rec.taxes_id.compute_all(price2, product=prod, partner=self.env['res.partner'])
                    rec.listprice_price2 = price2
                    rec.listprice_price2_vat = res['total_included']
                except:
                    rec.listprice_price2 = False
                    rec.listprice_price2_vat = False

class ProductProduct(models.Model):
    _inherit ='product.product'

    listprice_price = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta"
    )
    listprice_price2 = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2"
    )
    listprice_price_vat = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta c/iva"
    )
    listprice_price2_vat = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2 c/iva"
    )

    def _compute_price(self):
        listprice_tree_view = self.env.user.company_id.tree_view_pricelist_id.id
        listprice_tree_view2 = self.env.user.company_id.tree_view_pricelist2_id.id
        for rec in self:
            if rec:
                price = rec.with_context(pricelist=listprice_tree_view).price
                res = rec.taxes_id.compute_all(price, product=rec, partner=self.env['res.partner'])
                rec.listprice_price = price
                rec.listprice_price_vat = res['total_included']
                try:
                    price2 = rec.with_context(pricelist=listprice_tree_view2).price
                    res = rec.taxes_id.compute_all(price2, product=rec, partner=self.env['res.partner'])
                    rec.listprice_price2 = price2
                    rec.listprice_price2_vat = res['total_included']
                except:
                    rec.listprice_price2 = False
                    rec.listprice_price2_vat = False


