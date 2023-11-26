# -*- coding: utf-8 -*-

from odoo import tools
from odoo.tests.common import SingleTransactionCase, tagged, Form
from odoo.exceptions import ValidationError


@tagged("+student_management")
class TestStudent(SingleTransactionCase):
    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()
        cls.student = cls.env["student_management.student"].create(
            {
                "name": "Student",
                "email": "student@example.com",
                "user_id": cls.env.ref("base.user_admin").id,
            }
        )
        cls.teacher = cls.env["student_management.teacher"].create(
            {
                "name": "Teacher",
                "email": "teacher@example.com",
                "user_id": cls.env.ref("base.user_admin").id,
            }
        )
        cls.std_form = Form(cls.env["student_management.student"])
        cls.std_form.name = cls.student[0].name
        cls.std_form.user_id = cls.student[0].user_id
        cls.course_ids = cls.env["student_management.course"].create(
            {
                "name": "Course 1",
                "teacher_id": cls.teacher.id,
                "description": "Course 1's description",
            }
        )

    def test_create(self):
        self.assertEqual(self.student.user_id.id, self.env.ref("base.user_admin").id)
        self.std_form.age = 10
        try:
            self.std_form.save()
        except ValidationError as e:
            self.assertEqual(str(e), "Age must be between 18 and 60")

    def test__onchange_course_ids(self):
        self.std_form.age = 18
        self.std_form.course_ids.add(self.course_ids[0])
        self.std_form.save()
        channel = self.env["mail.channel"].search(
            [("name", "=", f"School - {self.teacher}")], limit=1
        )
        self.assertNotEqual(
            channel.channel_fetch_preview(),
            tools.plaintext2html(
                f'{self.student[0].name} is enrolled in "{self.course_ids[0].name}" course.'
            ),
        )
