# Copyright 2018 Tecnativa - Jairo Llopis
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Privacy - Consent",
    "summary": "Allow people to explicitly accept or reject inclusion "
    "in some activity, GDPR compliant",
    "version": "15.0.1.0.1",
    "development_status": "Production/Stable",
    "category": "Privacy",
    "website": "https://github.com/OCA/data-protection",
    "author": "Tecnativa, initOS GmbH, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["privacy"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_actions_server.xml",
        "data/ir_cron.xml",
        "data/mail.xml",
        "templates/form.xml",
        "views/privacy_consent.xml",
        "views/privacy_activity.xml",
        "views/res_partner.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "privacy_consent/static/src/css/privacy_consent.scss",
        ]
    },
}
