# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
#from gaepermission.decorator import login_not_required
from pedido.pedido_model import Pedido, PedidoForm
from config.template_middleware import TemplateResponse
from routes import pedidos
from tekton.gae.middleware.redirect import RedirectResponse


#@login_not_required
@no_csrf
def salvar(**kwargs):
    form = PedidoForm(**kwargs)
    erros=form.validate()

    if not erros:
        valores_normalizados = form.normalize()
        pedido = Pedido(**valores_normalizados)
        pedido.put()
        return RedirectResponse(pedidos)
    else:
        ctx={'pedido':kwargs,'erros':erros}
        return TemplateResponse(ctx,'pedidos/pedido_form.html')
