# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class PersonBase(models.AbstractModel):
    _name = "student_management.person.base"
    _description = "Basic Person"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    date_of_birth = fields.Date(string="Date of birth")
    age = fields.Integer(
        string="Age", compute="_compute_age", readonly=False, store=True
    )
    user_id = fields.Many2one(
        "res.users", string="User", required=True, ondelete="cascade"
    )

    @api.depends("date_of_birth")
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                delta_day = (fields.Date.today() - record.date_of_birth).days
                record.age = int(delta_day / 365.25)

    # TODO What about user set age manually after setting date of birth
    # @api.onchange("age")
    # def _onchange_date_begin(self):
    #     if self.age:
    #         self.date_of_birth = False

    def notify(self, msg=""):
        self.ensure_one()
        bot = self.env.ref("base.partner_root")
        channel_name = f"School - {self.user_id.name}"
        channel = self.env["mail.channel"].search(
            [("name", "=", channel_name)], limit=1
        ) or self.env["mail.channel"].create(
            {"name": channel_name, "channel_type": "group"}
        )
        channel.add_members((bot.id, self.user_id.partner_id.id))
        result = channel.message_post(
            author_id=bot.id,
            body=msg,
            message_type="comment",
            subtype_xmlid="mail.mt_comment",
        )
        return result
