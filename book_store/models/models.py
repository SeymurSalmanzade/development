# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book_store(models.Model):
    _name = 'book_store.book_store'
    _description = 'book_store.book_store'
    advance_genre = fields.Selection("_get_advence_genre_list")

    name = fields.Char()
    author = fields.Char()
    value = fields.Monetary(string="Value")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, store=True)
    description = fields.Text()

    def _get_advence_genre_list(self):
        return [('mystery','Mystery'),
                ('fantasy','Fantasy'),
                ('thriller','Thriller'),
                ('horror','Horror'),
                ('romance','Romance'),
                ('science','Science'),
                ('historical','Historical'),
                ('memoir','Memoir')]