from odoo import fields, api, models

class EstateProperty(models.Model):
  _name = 'estate.property'
  _description = 'Estate property'

  name = fields.Char(string='name', require=True, default="Unknown")
  description = fields.Text(string="Description")
  date_availability = fields.Date(string="Date availability", default=fields.Date.add(fields.Date.today(), months=3))
  expected_price = fields.Float()
  bedroom = fields.Integer(string="Bedroom", default=2)
  garden = fields.Boolean(string="Have garden")
  garden_orientation = fields.Selection(string="Orientation of garden",
  selection=[
    ("north", "North"),
    ("south", "South"),
    ("east", "East"),
    ("west", "West")
    ])
  active = fields.Boolean(string="Is Active", default=False)
  state = fields.Selection(string="State", selection=[
    ("new", "New"),
    ("offer_received", "Offer Received"),
    ("offer_accepted", "Offer Accepted"),
    ("sold", "Sold"), ("cancelled", "Cancelled")
    ], required=True, default="new", copy=False)