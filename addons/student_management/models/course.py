# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = "student_management.course"
    _description = "student_management.course"

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one(string="Teacher", comodel_name='student_management.teacher')