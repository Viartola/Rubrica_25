# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Set(models.Model):
    _name = 'lego.set'
    name = fields.Char(string="Nombre set", required=True)

    producto_id = fields.One2many('lego.producto','set_id', string="Producto")

class Producto(models.Model):
    _name = 'lego.producto'
    name = fields.Char(string="Nombre producto", required=True)
    pieces = fields.Integer(string="Numero de piezas", required=True)
    pieces_res = fields.Integer(string="Numero piezas de repuesto", required=True)

    total = fields.Integer(string="Total de piezas", compute='_calc_pie_tot')

    set_id = fields.Many2one('lego.set', string="Set")
    coleccionista = fields.Many2many('res.partner', 'producto_coleccionista', 'producto_id', 'coleccionista_id', 'Coleccionista')

    @api.one
    def _calc_pie_tot(self):
        if (self.pieces and self.pieces_res):
        	self.total = self.pieces + self.pieces_res


    @api.depends('pieces', 'pieces_res')
    def _piecesTotal(self):
        for r in self:
            if (r.pieces and r.pieces_res):
            	r.total = r.pieces + r.pieces_res     
                continue

class Coleccionista(models.Model):
    _inherit = 'res.partner'
    producto = fields.Many2many('lego.producto', 'producto_coleccionista', 'coleccionista_id', 'producto_id', 'Producto')
