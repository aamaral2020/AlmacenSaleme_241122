# -*- coding: utf-8 -*-
{
    'name': 'POS Payment Amount',
    'version': '0.1',
    'author': 'Ing. Gabriela Rivero',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': 'www.galup.com.ar',
    'description': 'This modules adds payment total amount in pos payment screen.',
    'depends': [
        'point_of_sale',
        'credit_card_instalment_pos',
    ],
    'data': [
    ],
    'assets': {
        "point_of_sale.assets": [
            "/pos_payment_amount/static/src/js/models.js",
            "/pos_payment_amount/static/src/js/PaymentScreenStatus.js",
            "/pos_payment_amount/static/src/js/PaymentScreen.js",
        ],
        'web.assets_qweb': [
            '/pos_payment_amount/static/src/xml/pos_payment_amount.xml',
        ],

    },
    'installable': True,
}
