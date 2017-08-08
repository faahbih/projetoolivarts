# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from desenho.desenho_model import Desenho, DesenhoForm
from pedido.pedido_model import PedidoForm, Pedido
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


@login_not_required
@no_csrf
def apagar(desenho_id):
    key = ndb.Key(Desenho, int(desenho_id))
    key.delete()
    return JsonUnsecureResponse('')


@login_not_required
@no_csrf
def listar():
    form = DesenhoForm()
    desenhos = Desenho.query_ordenada_por_nome().fetch()
    desenhos = [form.fill_with_model(p) for p in desenhos]
    return JsonUnsecureResponse(desenhos)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = DesenhoForm(**propriedades)
    erros = form.validate()
    if not erros:
        desenho = form.fill_model()
        desenho.put()
        dct = form.fill_with_model(desenho)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse(erros)
