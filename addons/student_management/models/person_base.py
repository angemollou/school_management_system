# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class PersonBase(models.AbstractModel):
    _name = "student_management.person.base"
    _description = "Basic Person"
    _order = 'name'

    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Float(string='Age', compute="_compute_age", readonly=False, store=True)

    @api.depends("date_of_birth")
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                delta_day = (fields.Date.today() - record.date_of_birth).days
                record.age = int(delta_day / 365.25)