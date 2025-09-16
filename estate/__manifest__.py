{
    "name": "Estate",  # The name that will appear in the App list
    "sumary": """summary""",
    "description": """this module is a module test for learn Odoo.""",
    "version": "18.0.1.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/test_model.xml",
        "views/estate_property_views.xml"
    ],
    "installable": True,
    'license': 'LGPL-3',
}
