# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
#from pedido.pedido_model import Pedido
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from pedido.pedido_model import Pedido, PedidoForm
from routes import pedidos
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path



@no_csrf
def index(pedido_id):
    pedido = Pedido.get_by_id(int(pedido_id))
    ctx={'pedido':pedido,
         'salvar_path':to_path(salvar)}
    return TemplateResponse(ctx,'pedidos/pedido_form.html')

def salvar(pedido_id,**kwargs):
    #pedido = Pedido.get_by_id(pedido_id)
    form = PedidoForm(**kwargs)
    erros = form.validate()

    if not erros:
        pedido = form.fill_model()
        pedido.put()
    return RedirectResponse(pedidos)
