# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student_management.student"
    _description = "student_management.student"
    _inherit = "student_management.person.base"

    # TODO basic (CRUD) operations existing
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
