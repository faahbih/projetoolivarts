# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from desenho.desenho_model import Desenho, DesenhoForm
from gaecookie.decorator import no_csrf
#from pedido.pedido_model import Pedido, PedidoForm
from routes import desenhos
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

@no_csrf
def index(desenho_id):
    desenhos = Desenho.get_by_id(int(desenho_id))
    ctx={'desenhos': desenhos,
         'salvar_path':to_path(salvar)}
    return TemplateResponse(ctx,'/desenhos/desenhos_form.html')

def salvar(desenho_id,**kwargs):
    desenhos = Desenho.get_by_id(desenho_id)
    desenho = DesenhoForm(**kwargs)
    desenho.put()
    return RedirectResponse(desenhos)
