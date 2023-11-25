# -*- coding: utf-8 -*-

import statistics
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = "student_management.course"
    _description = "student_management.course"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    teacher_id = fields.Many2one(
        string="Teacher",
        comodel_name="student_management.teacher",
        required=True,
        ondelete="restrict",
    )
    average_age = fields.Float(
        string="Average age of students", compute="_compute_average_age_of_students"
    )
    staff_id = fields.Many2one(string="Staff", comodel_name="student_management.staff")

    def _compute_average_age_of_students(self):
        self.env.cr.execute(
            """
            SELECT sc_rel.student_management_course_id, avg(st.age)
            FROM student_management_course_student_management_student_rel sc_rel
            LEFT JOIN student_management_student st ON sc_rel.student_management_student_id = st.id
            WHERE sc_rel.student_management_course_id IN %s
            GROUP BY sc_rel.student_management_course_id
            """,
            [tuple(self.ids)],
        )
        course_data = dict(self.env.cr.fetchall())  # {id: avg}
        for course in self:
            course.average_age = course_data.get(course.id, 0)
