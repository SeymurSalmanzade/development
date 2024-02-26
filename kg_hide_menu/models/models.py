# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kg_hide_menu(models.Model):
    _name = 'kg_hide_menu.kg_hide_menu'
    _description = 'kg_hide_menu.kg_hide_menu'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

