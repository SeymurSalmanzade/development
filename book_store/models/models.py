# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book_store(models.Model):
    _name = 'book_store.book_store'
    _description = 'This is a book store'
    
    genre = fields.Selection("_get_genre_list")
    def _get_genre_list(self):
        return [('mystery','Mystery'),
                ('fantasy','Fantasy'),
                ('thriller','Thriller'),
                ('horror','Horror'),
                ('romance','Romance'),
                ('science','Science'),
                ('historical','Historical'),
                ('memoir','Memoir')]

    name = fields.Char(copy=False, translate=True)
    is_new = fields.Boolean("New?", default=False, copy=False, required=True)
    author = fields.Char(copy=False, size=15)
    release_date = fields.Date("Release Date", copy=False, default=fields.Date.today)
    premiere_night = fields.Datetime(copy=False, default=fields.Datetime.now)
    value = fields.Monetary(string="Value", copy=False)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.AZN'), store=True, copy=False)
    description = fields.Text(copy=False, translate=True, help='Write some words for selling if you want')


class res_currency(models.Model):
    _inherit = 'res.currency'

    book_store_id = fields.One2many('book_store.book_store','currency_id')

class book_lists(models.Model):
    _name = 'book_lists'
    _description = 'This is the lists of books'

    name = fields.Char()
    name = fields.Char()
    name = fields.Char()
    name = fields.Char()
    name = fields.Char()
