# -*- coding: utf-8 -*-

# from odoo import fields, models, api

from odoo import fields, models, api
from jinja2 import Template
import logging
_logger = logging.getLogger(__name__)


class ResCompany(models.Model):

    _inherit = "res.company"
    _description = "Report add Company Logo ,Company Name & Background Image"

    upload_image = fields.Binary("Upload Image",
                                 attachment=True,
                                 help="This field holds the image used for" +
                                 "the badge, limited to 256x256")
    header = fields.Binary('Header')
    rotate_image = fields.Boolean(string='Rotate')
    watermark = fields.Boolean(string='Watermark')
    watermark_option = fields.Selection([
                                        ('logo', 'Company Logo'),
                                        ('name', 'Company Name'),
                                        ('backgroundimage', 'Background Image'
                                         )],
                                        default='logo', string="Watermark " +
                                        "Option")
    rotate_angle = fields.Char(string='Rotate Angle')

    font_size = fields.Char(string='Font Size', default=20)
    font_color = fields.Char(string="Font Color")

    @api.onchange('watermark')
    def onchange_watermark(self):
        if self.watermark:
            self.watermark_option = ""
            self.font_size = ""
            self.rotate_angle = ""
            self.font_size = ""
            self.font_color = ""
            self.upload_image = 0
            self.rotate_image = ""

    @api.onchange('watermark_option')
    def onchange_watermark_option(self):
        if self.watermark_option == 'backgroundimage':
            self.upload_image = 0
        if self.watermark_option == 'name':
            self.rotate_image = ""
            self.rotate_angle = ""
            self.font_size = ""
            self.font_color = ""

class SaleOrderTmlCustom(models.Model):
    _inherit = 'sale.order.template'

    logo = fields.Binary('Logo')
    body_html = fields.Html('Conteúdo da Proposta')
    contract_html = fields.Html('Conteúdo do Contrato')


class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'

    parent_order = fields.Many2one('sale.order', "Proposta Relacionada")

    def render_html(self, body_html):
        if not body_html:
            return ""
        body_html = body_html.replace("$PageBreak", "".join(["<br/>" for i in range(1, 11)]))
        tm = Template(body_html)
        msg = tm.render(object=self)

        _logger.warning(f'################# FIELD: {body_html} #################')
        _logger.warning(f'################# TEMPLATE: {tm} #################')
        _logger.warning(f'################# MESSAGE: {msg} #################')

        return msg