# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from desenho.desenho_model import DesenhoForm, Desenho
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from routes import desenhos
from tekton.gae.middleware.redirect import RedirectResponse


#@login_not_required
@no_csrf
def salvar(**kwargs):
    form = DesenhoForm(**kwargs)
    erros=form.validate()

    if not erros:
        valores_normalizados = form.normalize()
        desenho = Desenho(**valores_normalizados)
        desenho.put()
        return RedirectResponse(desenhos)
    else:
        ctx={'desenhos':kwargs,'erros':erros}
        return TemplateResponse(ctx,'desenhos/desenhos_form.html')
