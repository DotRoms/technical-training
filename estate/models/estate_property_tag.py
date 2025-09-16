from odoo import fields, models, api, _ 

class EstatePropertyTag(models.Model):
  _name = "estate.property.tag"
  _description = "Estate Property Tag"

  name = fields.Char(string="Name")