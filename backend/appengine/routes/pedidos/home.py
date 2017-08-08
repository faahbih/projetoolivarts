# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from pedido.pedido_model import Pedido
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.pedidos import edit
from routes.pedidos.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

@login_not_required
@no_csrf
def index():
    query = Pedido.query_ordenada_por_nome()
    pedidos = query.fetch()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)

    for ped in pedidos:
        key = ped.key
        id = key.id()
        ped.edit_path = to_path(edit_path_base, id)
        ped.deletar_path = to_path(deletar_path_base, id)

    salvar_path = to_path(salvar)
    ctx = {'salvar_path': salvar_path,
           'pedidos': pedidos}
    return TemplateResponse(ctx, 'pedidos/pedido_home.html')

def deletar(pedido_id):
    key = ndb.Key(Pedido, int(pedido_id))
    key.delete()
    return RedirectResponse(index)
