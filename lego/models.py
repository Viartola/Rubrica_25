# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Set(models.Model):
    _name = 'lego.set'
    name = fields.Char(string="Nombre set", required=True)
    producto_id = fields.One2many('lego.producto','set_id', string="Producto")

class Producto(models.Model):
    _name = 'lego.producto'
    name = fields.Char(string="Nombre producto", required=True)
    set_id = fields.Many2one('lego.set', string="Set")
    coleccionista = fields.Many2many('res.partner', 'producto_coleccionista', 'producto_id', 'coleccionista_id', 'Coleccionista')


class Coleccionista(models.Model):
    _inherit = 'res.partner'
    producto = fields.Many2many('lego.producto', 'producto_coleccionista', 'coleccionista_id', 'producto_id', 'Producto')
