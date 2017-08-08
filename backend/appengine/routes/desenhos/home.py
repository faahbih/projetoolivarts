# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from desenho.desenho_model import Desenho
from gaepermission.decorator import login_not_required
from pedido.pedido_model import Pedido, PedidoForm
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.desenhos import edit
from routes.desenhos.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index(desenho_selecionada = None):
    ctx ={'desenhos': Desenho.query_ordenada_por_nome().fetch(),
          'salvar_path': to_path(salvar),'pesquisar_path':to_path(index)}

    if desenho_selecionada is None:
        ctx['desenho_selecionada']=None
    else:
        ctx['desenho_selecionada']= Desenho.get_by_id(int(desenho_selecionada))
    return TemplateResponse(ctx,'desenhos/desenhos_home.html')



def salvar(**kwargs):
    form = PedidoForm(**kwargs)
    erros = form.validate()
    if not erros:
        desenhos = form.fill_model()
        desenhos.put()

def deletar(desenho_id):
    key = ndb.Key(Desenho, int(desenho_id))
    key.delete()
    return RedirectResponse(index)