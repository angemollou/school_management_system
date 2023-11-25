# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Staff(models.Model):
    _name = "student_management.staff"
    _description = "student_management.staff"
    _inherit = "student_management.person.base"

    position = fields.Char(string="Position")
    wage = fields.Monetary(string="Salary")
    course_ids = fields.Many2many("student_management.course", string="Courses")
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id,
    )
