from odoo import fields, api, models
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
class EstateProperty(models.Model):
  _name = 'estate.property'
  _description = 'Estate property'

  name = fields.Char(string='name', require=True, default="Unknown")
  description = fields.Text(string="Description")
  date_availability = fields.Date(string="Date availability", default=fields.Date.add(fields.Date.today(), months=3))
  expected_price = fields.Float()
  selling_price = fields.Float(string="Selling Price", readonly=True)
  living_area = fields.Float(string="Living Area")
  bedroom = fields.Integer(string="Bedroom", default=2)
  garden = fields.Boolean(string="Have garden")
  garden_area = fields.Float(string="Garden Area")
  postcode = fields.Integer(string="Postcode")
  garden_orientation = fields.Selection(string="Orientation of garden",
  selection=[
    ("north", "North"),
    ("south", "South"),
    ("east", "East"),
    ("west", "West")
    ])
  active = fields.Boolean(string="Is Active", default=True)
  state = fields.Selection(string="State", selection=[
    ("new", "New"),
    ("offer_received", "Offer Received"),
    ("offer_accepted", "Offer Accepted"),
    ("sold", "Sold"),
    ("cancelled", "Cancelled")
    ], required=True, default="new", copy=False)
  property_type_id = fields.Many2one("estate.property.type", string="Property Type")
  buyer_id = fields.Many2one("res.partner", string="buyer", required=True)
  salesperson_id = fields.Many2one("res.users", string="saler", copy=False, default=lambda self: self.env.user, required=True)
  tag_ids = fields.Many2many("estate.property.tag", string="Tag(s)")
  offer_ids = fields.One2many("estate.property.offer", "property_id")
  total_area = fields.Float(compute="_compute_total_area", readonly=True)
  best_price = fields.Float(compute="_compute_best_price")


  @api.depends("living_area", "garden_area")
  def _compute_total_area(self):
    for record in self:
      record.total_area = record.living_area + record.garden_area


  @api.depends("offer_ids")
  def _compute_best_price(self):
    for record in self:
      if record.offer_ids:
        record.best_price = max(record.offer_ids.mapped("price"))
      else:
        record.best_price = 0


  @api.onchange("garden")
  def add_value_of_garden(self):
    for record in self:
        record.garden_area = 10 if record.garden else 0
        record.garden_orientation = "north" if record.garden else False
      

  def cancel(self):
    for record in self:
      if record.state not in ['sold']:
        record.state = "cancelled"


  def sold(self):
    for record in self:
      if record.state not in ['cancelled']:
        record.state = "sold"

  @api.constrains("expected_price", "selling_price", "best_price")
  def _check_positive_price(self):
    for record in self:
      if record.expected_price < 0 or record.selling_price < 0 or record.best_price < 0:
        raise ValidationError("You must set a positive price")
