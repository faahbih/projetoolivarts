# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from drawing.drawing_model import Drawing
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.resti.pedidos import salvar
from routes.resti.pedidos import index
from routes.resti.pedidos import apagar
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


@login_not_required
@no_csrf
def index():
    salvar_path = to_path(salvar)
    listar_path = to_path(index)
    apagar_path = to_path(apagar)

    ctx = {'salvar_path': salvar_path,
           'apagar_path': apagar_path,
           'listar_path': listar_path}

    return TemplateResponse(ctx, 'pedido/pedidoHome.html')


@login_not_required
def deletar(pedido_id):
    key = ndb.Key(Drawing, int(pedido_id))
    key.delete()
    return RedirectResponse(index)
