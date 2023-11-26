# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tests.common import TransactionCase, tagged, Form


@tagged("+student_management")
class TestPersonBase(TransactionCase):
    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()
        cls.teacher = cls.env["student_management.teacher"].create(
            {
                "name": "Teacher",
                "email": "teacher@example.com",
                "user_id": cls.env.ref("base.user_demo").id,
            }
        )
        cls.std_form = Form(cls.env["student_management.teacher"])
        cls.std_form.name = cls.teacher[0].name

    def test__compute_age(self):
        self.std_form.user_id = self.teacher[0].user_id
        self.std_form.date_of_birth = "1999-01-01"
        self.std_form.save()
        timedelta = fields.Date.today() - fields.Date.from_string(
            self.std_form.date_of_birth
        )
        self.assertEqual(self.std_form.age, timedelta.days // 365.25)
