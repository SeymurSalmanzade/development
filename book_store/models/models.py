# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book_store(models.Model):
    _name = 'book_store.book_store'
    _description = 'This is a book store'

    genres = fields.Many2many("genre_list","book_genre_relation","book_store","genre_list",
                             required=True, help='Select at least one genre')
    
    # genre = fields.Selection("_get_genre_list")
    # def _get_genre_list(self):
    #     return [('mystery','Mystery'),
    #             ('fantasy','Fantasy'),
    #             ('thriller','Thriller'),
    #             ('horror','Horror'),
    #             ('romance','Romance'),
    #             ('science','Science'),
    #             ('historical','Historical'),
    #             ('memoir','Memoir')]

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

    book_lists_id = fields.One2many('book_store.book_store','currency_id')
    movie_lists_id = fields.One2many('movie_list','currency_id')

class movie_list(models.Model):
    _name = 'movie_list'
    _description = 'This is the list of movies'

    categories = fields.Many2many("category_list","movie_categorie_relation","movie_list","category_list",
                            required=True, help='Select at least one category')

    # category = fields.Selection("_get_category_list")
    # def _get_category_list(self):
    #     return [('mystery','Mystery'),
    #             ('fantasy','Fantasy'),
    #             ('crime','Crime'),
    #             ('thriller','Thriller'),
    #             ('horror','Horror'),
    #             ('romance','Romance'),
    #             ('science','Science'),
    #             ('blu-ray','Blu-Ray'),
    #             ('western','Western'),
    #             ('historical','Historical'),
    #             ('documentary','Documentary'),
    #             ('memoir','Memoir')]

    name1 = fields.Char("Name",copy=False, translate=True)
    name2 = fields.Selection([('yes','Yes'),('no','No')],"New?", required=True)
    author = fields.Char(copy=False, size=15)
    release_date = fields.Date("Release Date", copy=False, default=fields.Date.today)
    premiere_night = fields.Datetime(copy=False, default=fields.Datetime.now)
    value = fields.Monetary(string="Value", copy=False)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.AZN'), store=True, copy=False)
    description = fields.Html(copy=False, help='Write some words for selling if you want')


class genre_list(models.Model):
    _name = 'genre_list'
    _description = 'This is the genre list'

    name = fields.Char()
    color = fields.Integer()
    # fantasy = fields.Char("Fantasy")
    # thriller = fields.Char("Thriller")
    # horror = fields.Char("Horror")
    # romance = fields.Char("Romance")
    # science = fields.Char("Science")
    # historical = fields.Char("Historical")
    # memoir = fields.Char("Memoir")

class category_list(models.Model):
    _name = 'category_list'
    _description = 'This is the category list'

    name = fields.Char()
    color = fields.Integer()
    # fantasy = fields.Char("Fantasy")
    # crime = fields.Char("Crime")
    # thriller = fields.Char("Thriller")
    # horror = fields.Char("Horror")
    # romance = fields.Char("Romance")
    # science = fields.Char("Science")
    # blu-Ray = fields.Char("Blu-Ray")
    # western = fields.Char("Western")
    # historical = fields.Char("Historical")
    # documentary = fields.Char("Documentary")
    # memoir = fields.Char("Memoir")