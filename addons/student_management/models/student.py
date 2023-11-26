# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student_management.student"
    _description = "student_management.student"
    _inherit = "student_management.person.base"

    course_ids = fields.Many2many("student_management.course", string="Courses")

    # basic (CRUD) operations existing
    # by default are create(),read(),write(),unlink()
    # Don't need to override some of them for now

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "age" in vals:
                if vals["age"] < 18 or vals["age"] > 60:
                    raise ValidationError(_("Age must be between 18 and 60"))
        res_ids = super().create(vals_list)
        return res_ids

    @api.onchange("course_ids")
    def _onchange_course_ids(self):
        if self.ids:
            db_course_ids = self.browse(self.ids[0]).course_ids.ids
            ui_course_ids = self.course_ids.ids
            new_courses = set(ui_course_ids) - set(db_course_ids)
            new_courses = self.env["student_management.course"].browse(new_courses)
            for course in new_courses:
                course.teacher_id.notify(
                    f'{self.name} is enrolled in "{course.name}" course.'
                )
