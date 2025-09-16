from odoo import fields, models, api, _

class EstatePropertyType(models.Model):
  _name = "estate.property.type"
  _description = "Estate Property Type"

  name = fields.Char(string="Name")
