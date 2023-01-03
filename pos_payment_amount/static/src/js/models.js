odoo.define('pos_payment_amount.models', function (require) {
    console.log('pos_payment_amount');

    var models = require('point_of_sale.models');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;

    var posorder_super = models.Order.prototype;

    models.Order = models.Order.extend({

        get_acum: function(paymentline) {
            console.log('paymentline', paymentline)
            var acum = 0
            var lines = this.paymentlines.models;
            for (var i = 0; i < lines.length; i++) {
                if (lines[i] === paymentline) {
                    break;
                } else {
                    acum += lines[i].get_amount();
                }
            }
            return round_pr(acum, this.pos.currency.rounding);
        },

        remove_paymentline: function(line) {
            let order = this.pos.get_order();
            var lines = order.get_orderlines();
            if (line['payment_method']['type']=='cash') {
                var product  = this.pos.db.get_product_by_id(this.pos.config.saleme_discount_product_id[0]);
            }
            else {
                var product  = this.pos.db.get_product_by_id(line['payment_method']['instalment_product_id'][0]);
            }
            // Remove existing discounts
            for (const line of lines) {
                if (line.get_product() === product) {
                    order.remove_orderline(line);
                }
            }
            posorder_super.remove_paymentline.apply(this, arguments);
        }

    });

});