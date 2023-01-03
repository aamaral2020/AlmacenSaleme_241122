odoo.define('pos_payment_amount.PaymentScreenStatus', function(require) {
    'use strict';

    const PaymentScreenStatus = require('point_of_sale.PaymentScreenStatus');
    const Registries = require('point_of_sale.Registries');

    const PosResPaymentScreenStatus = PaymentScreenStatus =>
        class extends PaymentScreenStatus {
            constructor() {
                super(...arguments);
            }

            // clickBack() {
            //     this.showScreen('ProductScreen');
            // }
            get acumText() {
                return this.env.pos.format_currency(
                    this.currentOrder.get_acum() > 0 ? this.currentOrder.get_acum() : 0
                );
            }
        };

    Registries.Component.extend(PaymentScreenStatus, PosResPaymentScreenStatus);

    return PosResPaymentScreenStatus;
});