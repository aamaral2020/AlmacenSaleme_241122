odoo.define('pos_payment_amount.models', function (require) {
    console.log('pos_payment_amount');

    var models = require('point_of_sale.models');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;

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

    });

});