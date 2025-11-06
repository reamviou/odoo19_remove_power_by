# -*- coding: utf-8 -*-
{
    'name': "Remove Powered By",
    'author': 'V Technologies',
    'website': 'https://apps.odoo.com/apps/modules/browse?search=vitou',
    'maintainer': 'V Technologies',
    'version': '19.0.1.1.1',
    'category': 'Website',
    'sequence': 75,
    'summary': 'Remove Powered By',
    #'price':'10.0',
    #'currency':'USD',
    'description': "Remove Powered By",
    'depends': [
        'web'
        # 'website_sale',
        # 'hr.employee',

    ],
    'data': [

        'views/remove_powered_by.xml',

    ],
    # 'assets': {
    #         'point_of_sale._assets_pos': [
    #             'vitou_remove_powered_by/static/src/xml/remove_powered_by.xml',
    #
    #         ],
    #
    #     },

    'images': ['static/description/banner.png'],
    "installable": True,
    "application": True,
    "auto_install": False,
    'license': 'OPL-1',
}
