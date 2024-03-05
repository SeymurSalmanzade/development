# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book_store(models.Model):
    _name = 'book_store.book_store'
    _description = 'book_store.book_store'
    genre = fields.Selection("_get_genre_list")

    name = fields.Char(default=lambda self: self.env.user.name)
    value = fields.Monetary(string="Value")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, store=True)
    description = fields.Text()

    def _get_genre_list(self):
        return [('mystery','Mystery'),
                ('fantasy','Fantasy'),
                ('thriller','Thriller'),
                ('horror','Horror'),
                ('romance','Romance'),
                ('science','Science'),
                ('historical','Historical'),
                ('memoir','Memoir')]

class res_currency(models.Model):
    _inherit = "res.currency"

    name = fields.Char()
    book_store_id = fields.One2many('book_store.book_store','currency_id')
