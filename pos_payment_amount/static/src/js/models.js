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

        get_acum_no_cash: function(paymentline) {
            console.log('paymentline', paymentline)
            var acum = 0
            var lines = this.paymentlines.models;
            for (var i = 0; i < lines.length; i++) {
                if (lines[i] === paymentline) {
                    break;
                } else {
                    if (lines[i]['payment_method']['type']=='cash') {
                        continue;
                    } else {
                        acum += lines[i].get_amount();
                    }
                }
            }
            return round_pr(acum, this.pos.currency.rounding);
        },

        get_discount_lines: function(paymentline) {
            var lines = this.paymentlines.models;
            var due = 0;
            var product  = this.pos.db.get_product_by_id(this.pos.config.saleme_discount_product_id[0]);
            this.orderlines.each(function(line){

                console.log('due line', line)
                if (line.get_product() === product) {
                    due += line.get_price_with_tax();
                }
            });
            return round_pr(due, this.pos.currency.rounding);
        },

        get_acum_cash: function(paymentline) {
            console.log('paymentline', paymentline)
            var acum_cash = 0
            var lines = this.paymentlines.models;
            for (var i = 0; i < lines.length; i++) {
                if (lines[i] === paymentline) {
                    break;
                } else {
                    if (lines[i]['payment_method']['type']!='cash') {
                        continue;
                    } else {
                        acum_cash += lines[i].get_amount();
                    }
                }
            }
            var total = this.pos.get_order().get_total_with_tax() - this.pos.get_order().get_discount_lines();
            var acum = this.pos.get_order().get_acum_no_cash();
            var due = total - acum;
            if (acum_cash > due && due != 0) {
                acum_cash = due;
            }
            var pc = this.pos.config.saleme_discount_pc;
            var discount = acum_cash - (pc / 100.0 * acum_cash);
            // discount = discount / 1.21

            // product_id = this.pos.db.get_product_by_id[this.pos.config.saleme_discount_product_id[0]];
            // console.log('product_id.....----', product_id)
            // // console.log('product tax.....----', this.pos.config.saleme_discount_product_id.taxes_id)
            // var tax = this.pos.taxes_by_id[product_id];
            // console.log('tax', tax)
            // if (tax['price_include'] == false) {
            //     let calc_tax = (tax['amount']/100)+1;
            //     discount = discount/(calc_tax);
            //     discount = Math.round(discount * 100) / 100
            // }
            return round_pr(discount, this.pos.currency.rounding);
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