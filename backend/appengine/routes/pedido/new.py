# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from drawing.drawing_model import DrawingForm, Drawing
from routes import pedido
from tekton.gae.middleware.redirect import RedirectResponse
from gaepermission.decorator import login_not_required


@login_not_required
def salvar(**kwargs):
    form = DrawingForm(**kwargs)
    erros = form.validate()

    if not erros:
        valores_normalizados = form.normalize()
        pedidos = Drawing(**valores_normalizados)
        pedidos.put()
        return RedirectResponse(pedido)

    else:
        ctx = {'pedido': kwargs, 'erros': erros}
        return TemplateResponse(ctx, 'pedido/pedidoForm.html')
