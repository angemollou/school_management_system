# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = "student_management.Student"
    _description = "student_management.Student"

    name = fields.Char()
    date_of_birth = fields.Date()
    age = fields.Float(compute="_compute_age")

    @api.depends("date_of_birth")
    def _compute_age(self):
        for record in self:
            delta_day = (fields.Date.today() - record.date_of_birth).days
            record.age = int(delta_day / 365.25)

    # TODO basic (CRUD) operations existing
    # by default are create(),read(),write(),unlink()
    # Don't need to override them for now
