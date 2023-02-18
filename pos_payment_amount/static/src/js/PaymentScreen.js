odoo.define('pos_payment_amount.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const PosResPaymentScreen = PaymentScreen =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);

                // this.click_paymentmethods(this.env.pos.config.saleme_cash_id[0]);
                var cash_id = this.env.pos.config.saleme_cash_id;
                // this.addNewPaymentLine(cash_id[0]);
            }

            // clickBack() {
            //     this.showScreen('ProductScreen');
            // }
            // get acumText() {
            //     return this.env.pos.format_currency(
            //         this.currentOrder.get_acum() > 0 ? this.currentOrder.get_acum() : 0
            //     );
            // }
        };

    Registries.Component.extend(PaymentScreen, PosResPaymentScreen);

    return PosResPaymentScreen;
});