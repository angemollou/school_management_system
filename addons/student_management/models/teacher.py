# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teacher(models.Model):
    _name = "student_management.teacher"
    _description = "student_management.teacher"
    _inherit = "student_management.person.base"

    subject = fields.Char(string="Subject")
