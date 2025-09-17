from odoo import fields, models, api, _

class EstatePropertyType(models.Model):
  _name = "estate.property.type"
  _description = "Estate Property Type"
  _order = "name"

  name = fields.Char(string="Name")
  property_ids = fields.One2many("estate.property", "property_type_id")
  