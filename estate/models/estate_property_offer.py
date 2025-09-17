from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class EstatePropertyOffer(models.Model):
  _name = "estate.property.offer"
  _description = "Estate Property Offer"
  _order = "price desc"
  
  price = fields.Float()
  status = fields.Selection(copy=False, selection=[
    ("accepted", "Accepted"),
    ("refused", "Refused")
  ])
  partner_id = fields.Many2one("res.partner", required=True)
  property_id = fields.Many2one("estate.property", required=True)
  validity = fields.Integer(default=7, string="Validity")
  date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", string="Date Deadline")

  @api.depends("create_date", "validity")
  def _compute_date_deadline(self):
    for record in self:
      create_date = record.create_date or fields.Date.today()
      record.date_deadline = fields.Date.add(create_date, days=record.validity)

  def _inverse_date_deadline(self):
    for record in self:
      record.validity = (record.date_deadline - fields.Date.to_date(record.create_date)).date

  def accept(self):
    for record in self:
      record.status = "accepted"
      record.property_id.selling_price = record.price if record.status == "accepted" else 0

  def refuse(self):
    for record in self:
      record.status = "refused"