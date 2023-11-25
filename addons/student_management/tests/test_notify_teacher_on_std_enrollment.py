# -*- coding: utf-8 -*-

from odoo import SUPERUSER_ID, tools
from odoo.tests.common import TransactionCase, tagged


@tagged("+student_management")
class TestTeacherGetNotified(TransactionCase):
    def test_teacher_notify(self):
        teacher = self.env["student_management.teacher"].create(
            {
                "name": "Teacher",
                "email": "teacher@example.com",
                "user_id": self.env.ref("base.user_admin").id,
            }
        )
        self.assertEqual(
            teacher.notify("Just a message!").body,
            tools.plaintext2html("Just a message!"),
        )
        self.assertNotEqual(teacher.notify("Just a message!").body, "Just a message!")
