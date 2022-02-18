from odoo import fields, models
from jinja2 import Template
import logging
_logger = logging.getLogger(__name__)

class SaleOrderTmlCustom(models.Model):
    _inherit = 'sale.order.template'

    logo = fields.Binary('Logo')
    header = fields.Binary('Header')
    footer = fields.Binary('Footer')
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