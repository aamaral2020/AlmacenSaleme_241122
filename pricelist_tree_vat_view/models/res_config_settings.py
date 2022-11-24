   ##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    tree_view_pricelist_id = fields.Many2one(
        related='company_id.tree_view_pricelist_id',
        readonly=False,
    )
    tree_view_pricelist2_id = fields.Many2one(
        related='company_id.tree_view_pricelist2_id',
        readonly=False,
    )

class ResCompany(models.Model):
    _inherit = 'res.company'

    tree_view_pricelist_id = fields.Many2one(
        'product.pricelist',
        'Pricelist tree view',
    )
    tree_view_pricelist2_id = fields.Many2one(
        'product.pricelist',
        'Pricelist tree view 2',
    )
